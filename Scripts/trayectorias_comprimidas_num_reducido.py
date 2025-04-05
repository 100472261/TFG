import os
import zipfile
import numpy as np
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt

def graficar_rutas(puntos, id, zipf):
    # Separar coordenadas
    coordenadas_y, coordenadas_x = zip(*puntos)

    # Crear figura
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(coordenadas_x, coordenadas_y, linestyle="-", lw='3', color="k", label="Simplificada")
    ax.set_xticks([])
    ax.set_yticks([])

    # Guardar imagen en buffer
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    plt.close(fig)
    img_buffer.seek(0)

    # Escribir imagen al zip
    zipf.writestr(f"Trayectoria_comprimida_{id}.png", img_buffer.read())

if __name__ == "__main__":
    df_path = "./Trayectorias/Tipos_de_barcos/longitud_8/Tanker_modificado_compressed_8_v2.csv"
    df = pd.read_csv(df_path)

    trajectory_ids = df['Trajectory_ID'].unique()
    img_dir = "./Imagenes/Trayectorias_comprimidas/longitud_8"
    os.makedirs(img_dir, exist_ok=True)

    zip_filename = os.path.join(img_dir, "Trayectorias_Tanker_8.zip")
    trayectorias_omitidas = 0

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for id in trajectory_ids:
            df_trayectoria = df[df['Trajectory_ID'] == id]
            latitudes = df_trayectoria['Latitude'].tolist()
            longitudes = df_trayectoria['Longitude'].tolist()

            puntos = list(zip(latitudes, longitudes))
            graficar_rutas(puntos, id, zipf)

    print(f"¡Listo! Se guardaron las trayectorias en {zip_filename}")
    print(f"Trayectorias omitidas por falta de datos: {trayectorias_omitidas}")
