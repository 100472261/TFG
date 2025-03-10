import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

def graficar_rutas(puntos_originales, puntos_simplificados, id):
    coordenadas_y, coordenadas_x = zip(*puntos_originales)
    coordenadas_y_s, coordenadas_x_s = zip(*[puntos_originales[i] for i in puntos_simplificados])

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(coordenadas_x, coordenadas_y, marker="o", linestyle="-", color="b", label="Original")
    ax.plot(coordenadas_x_s, coordenadas_y_s, marker="x", linestyle="-", color="r", label="Simplificada")
    ax.legend()
    plt.savefig(f"./Imagenes/Pruebas_compresion/Trayectoria_comprimida_{id}.png")
    plt.close(fig)

if __name__ == "__main__":
    df_path = "./Trayectorias/Tipos_de_barcos/Cargo_modificado.csv"
    df = pd.read_csv(df_path)

    trajectory_ids = df['Trajectory_ID'].unique()

    trajectory_ids = [21]

    for id in trajectory_ids:
        latitudes = df[df['Trajectory_ID'] == id]['Latitude'].tolist()
        longitudes = df[df['Trajectory_ID'] == id]['Longitude'].tolist()
        puntos_iniciales = np.array(list(zip(latitudes, longitudes)))

        if len(puntos_iniciales) < 3:
            continue

        puntos_finales = [0]
        epsilon = 0.00005

        rdp(0, len(puntos_iniciales) - 1, puntos_iniciales, puntos_finales, epsilon)

        puntos_finales.append(len(puntos_iniciales) - 1)
        puntos_finales = sorted(puntos_finales)
        print(puntos_finales)
        graficar_rutas(puntos_iniciales, puntos_finales, id)
