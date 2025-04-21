import os
import zipfile
import numpy as np
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
from bearing import calcular_bearing

#Calcula la proyección escalar del punto p sobre la línea entre a y b
def calcular_proyeccion_escalar(p, a, b):
    ap = p - a
    ab = b - a
    ab_norm = np.linalg.norm(ab)

    if ab_norm == 0:
        return 0

    return np.dot(ap, ab) / ab_norm

#Calcula la distancia del punto c al segmento de línea entre a y b
def distancia_punto_a_recta(c, a, b):
    ab = b - a
    ab_norm = np.linalg.norm(ab)

    if ab_norm == 0:
        return np.linalg.norm(c - a)

    norm = calcular_proyeccion_escalar(c, a, b)

    if norm < 0:
        proyeccion = a
    elif norm > ab_norm:
        proyeccion = b
    else:
        proyeccion = a + (norm / ab_norm) * ab

    return np.linalg.norm(c - proyeccion)

#Encuentra el punto más alejado del segmento entre startIndex y endIndex
def encontrar_punto_mas_alejado(puntos_iniciales, startIndex, endIndex, epsilon):
    max_distancia = 0
    indice_punto_mas_alejado = -1

    for i in range(startIndex + 1, endIndex):
        distancia = distancia_punto_a_recta(puntos_iniciales[i], puntos_iniciales[startIndex], puntos_iniciales[endIndex])

        if distancia > max_distancia:
            max_distancia = distancia
            indice_punto_mas_alejado = i

    return indice_punto_mas_alejado if max_distancia > epsilon else -1

#Algoritmo Douglas-Peucker mediante índices
def rdp(startIndex, endIndex, puntos_iniciales, puntos_finales, epsilon):
    if startIndex >= endIndex:
        return

    proximo_punto = encontrar_punto_mas_alejado(puntos_iniciales, startIndex, endIndex, epsilon)

    if proximo_punto != -1:
        rdp(startIndex, proximo_punto, puntos_iniciales, puntos_finales, epsilon)
        puntos_finales.append(proximo_punto)
        rdp(proximo_punto, endIndex, puntos_iniciales, puntos_finales, epsilon)

#Ajusta el número de puntos en la trayectoria simplificada
def ajustar_numero_de_puntos(puntos_finales, num_puntos_deseados, puntos_iniciales):
    #Añade puntos dividiendo los segmentos más largos
    while len(puntos_finales) < num_puntos_deseados:
        max_gap = 0
        index_to_insert = -1

        for i in range(len(puntos_finales) - 1):
            gap = puntos_finales[i + 1] - puntos_finales[i]
            if gap > max_gap:
                max_gap = gap
                index_to_insert = i

        if index_to_insert != -1:
            new_point = (puntos_finales[index_to_insert] + puntos_finales[index_to_insert + 1]) // 2
            if new_point not in puntos_finales:
                puntos_finales.insert(index_to_insert + 1, new_point)

    #Elimina los puntos con menor impacto geométrico
    while len(puntos_finales) > num_puntos_deseados:
        min_error = float('inf')
        index_to_remove = -1

        for i in range(1, len(puntos_finales) - 1):
            d = distancia_punto_a_recta(
                puntos_iniciales[puntos_finales[i]], 
                puntos_iniciales[puntos_finales[i - 1]], 
                puntos_iniciales[puntos_finales[i + 1]]
            )

            if d < min_error:
                min_error = d
                index_to_remove = i

        if index_to_remove != -1:
            puntos_finales.pop(index_to_remove)

def graficar_rutas(puntos_originales, puntos_simplificados, id):
    #coordenadas_y, coordenadas_x = zip(*puntos_originales)
    coordenadas_y_s, coordenadas_x_s = zip(*[puntos_originales[i] for i in puntos_simplificados])
    
    fig, ax = plt.subplots(figsize=(6, 6))
    #ax.plot(coordenadas_x, coordenadas_y, marker="o", linestyle="-", color="b", label="Original")
    ax.plot(coordenadas_x_s, coordenadas_y_s, linestyle="-", lw='3', color="k", label="Simplificada")
    ax.set_xticks([])
    ax.set_yticks([])
    #ax.legend()

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    plt.close(fig)
    img_buffer.seek(0)

    zipf.writestr(f"Trayectoria_comprimida_{id}.png", img_buffer.read())

#Crea un nuevo .csv con la información de la trayectoria comprimida
def guardar_puntos_seleccionados(df, indices_puntos_finales, trajectory_id, output_file, first_write):
    df_seleccionado = df.iloc[indices_puntos_finales].copy()
    df_seleccionado['Trajectory_ID'] = trajectory_id
    df_seleccionado['Latitude_2'] = df_seleccionado['Latitude'].shift(-1)
    df_seleccionado['Longitude_2'] = df_seleccionado['Longitude'].shift(-1)
    df_seleccionado['Bearing'] = calcular_bearing(df_seleccionado['Latitude'], df_seleccionado['Longitude'], df_seleccionado['Latitude_2'], df_seleccionado['Longitude_2'])
    mode = 'w' if first_write else 'a'
    header = first_write
    df_seleccionado.to_csv(output_file, mode=mode, index=False, header=header, float_format='%.15g')  # Ensure full precision

if __name__ == "__main__":

    #df_path = "./Trayectorias/Tipos_de_barcos/v4/Cargo_modificado_v4.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/v4/Fishing_modificado_v4.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/v4/Military_modificado_v4.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/v4/Sailing_modificado_v4.csv"
    df_path = "./Trayectorias/Tipos_de_barcos/v4/Tanker_modificado_v4.csv"

    df = pd.read_csv(df_path)

    trajectory_ids = df['Trajectory_ID'].unique()

    img_dir = "./Imagenes/Trayectorias_comprimidas/longitud_8"
    os.makedirs(img_dir, exist_ok=True)

    #zip_filename = os.path.join(img_dir, "Compressed_Cargo_8_v4.zip")
    #zip_filename = os.path.join(img_dir, "Compressed_Fishing_8_v4.zip")
    #zip_filename = os.path.join(img_dir, "Compressed_Military_8_v4.zip")
    #zip_filename = os.path.join(img_dir, "Compressed_Sailing_8_v4.zip")
    zip_filename = os.path.join(img_dir, "Compressed_Tanker_8_v4.zip")

    output_dir = "./Trayectorias/Tipos_de_barcos/longitud_8"
    os.makedirs(output_dir, exist_ok=True)

    #output_file = os.path.join(output_dir, f"Cargo_modificado_compressed_8_v4_COMPLETO.csv")
    #output_file = os.path.join(output_dir, f"Fishing_modificado_compressed_8_v4_COMPLETO.csv")
    #output_file = os.path.join(output_dir, f"Military_modificado_compressed_8_v4_COMPLETO.csv")
    #output_file = os.path.join(output_dir, f"Sailing_modificado_compressed_8_v4_COMPLETO.csv")
    output_file = os.path.join(output_dir, f"Tanker_modificado_compressed_8_v4_COMPLETO.csv")

    num_puntos_deseados = 8
    trayectorias_omitidas = 0

    first_write = True

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for id in trajectory_ids:
            latitudes = df[df['Trajectory_ID'] == id]['Latitude'].tolist()
            longitudes = df[df['Trajectory_ID'] == id]['Longitude'].tolist()
            puntos_iniciales = np.array(list(zip(latitudes, longitudes)))
            
            if len(puntos_iniciales) < num_puntos_deseados:
                trayectorias_omitidas += 1
                continue
            
            indices_puntos_finales = [0]
            epsilon = 0.00005
            rdp(0, len(puntos_iniciales) - 1, puntos_iniciales, indices_puntos_finales, epsilon)
            indices_puntos_finales.append(len(puntos_iniciales) - 1)
            indices_puntos_finales = sorted(indices_puntos_finales)
            
            ajustar_numero_de_puntos(indices_puntos_finales, num_puntos_deseados, puntos_iniciales)
            
            graficar_rutas(puntos_iniciales, indices_puntos_finales, id)
            
            df_trayectoria = df[df['Trajectory_ID'] == id]
            guardar_puntos_seleccionados(df_trayectoria, indices_puntos_finales, id, output_file, first_write)
            first_write = False

    print(f"Imágenes comprimidas y guardadas OK !!!. Se han omitido {trayectorias_omitidas} trayectorias")
