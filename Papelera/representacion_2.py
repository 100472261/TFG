import os
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

def normalizar(value, min_val, max_val, new_min, new_max):
    if max_val == min_val:
        return (new_min + new_max) // 2
    return int((value - min_val) / (max_val - min_val) * (new_max - new_min) + new_min)

#df_path = "./Trayectorias/Tipos_de_barcos/Cargo_modificado.csv"
#df_path = "./Trayectorias/Tipos_de_barcos/Container_modificado.csv"
#df_path = "./Trayectorias/Tipos_de_barcos/Cruise_modificado.csv"
#df_path = "./Trayectorias/Tipos_de_barcos/Fishing_modificado.csv"
df_path = "./Trayectorias/Tipos_de_barcos/Tanker_modificado.csv"

df = pd.read_csv(df_path)

trajectory_ids = df['Trajectory_ID'].unique()

img_dir = "./Imagenes/Representacion_2"

#zip_filename = os.path.join(img_dir, "Cargo.zip")
#zip_filename = os.path.join(img_dir, "Container.zip")
#zip_filename = os.path.join(img_dir, "Cruise.zip")
#zip_filename = os.path.join(img_dir, "Fishing.zip")
zip_filename = os.path.join(img_dir, "Tanker.zip")

os.makedirs(img_dir, exist_ok=True)

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for id in trajectory_ids:
        lista_latitudes = df[df['Trajectory_ID'] == id]['Latitude'].tolist()
        lista_longitudes = df[df['Trajectory_ID'] == id]['Longitude'].tolist()

        if not lista_latitudes or not lista_longitudes:
            print(f"Advertencia: Trayectoria {id} no tiene datos válidos y será omitida.")
            continue

        lat_min, lat_max = min(lista_latitudes), max(lista_latitudes)
        lon_min, lon_max = min(lista_longitudes), max(lista_longitudes)

        coordenadas_pix = []

        for lat, lon in zip(lista_latitudes, lista_longitudes):
            coordenadas_pix.append((normalizar(lat, lat_min, lat_max, 0, 99), normalizar(lon, lon_min, lon_max, 0, 99)))

        #Trayectorias sin variación en latitud o longitud
        if lat_min == lat_max and lon_min == lon_max:
            #Caso: Trayectoria es un solo punto
            print(f"Trayectoria {id}: Sin variación en latitud ni longitud")
            coordenadas_pix = [coordenadas_pix[0]] * 5
        elif lat_min == lat_max:
            #Caso: Latitud constante
            print(f"Trayectoria {id}: Latitud constante")
            coordenadas_pix = [(normalizar(lat_min, lat_min, lat_max, 0, 99), normalizar(lon, lon_min, lon_max, 0, 99)) for lon in lista_longitudes]
        elif lon_min == lon_max:
            #Caso: Longitud constante -> Línea horizontal
            print(f"Trayectoria {id}: Longitud constante")
            coordenadas_pix = [(normalizar(lat, lat_min, lat_max, 0, 99), normalizar(lon_min, lon_min, lon_max, 0, 99)) for lat in lista_latitudes]

        coordenadas_y, coordenadas_x = zip(*coordenadas_pix)

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.plot(coordenadas_x, coordenadas_y, marker="o", linestyle="-", color="b", mfc="k")

        img_buffer = BytesIO()
        plt.savefig(img_buffer, format="png")
        plt.close(fig)
        img_buffer.seek(0)

        zipf.writestr(f"Trayectoria_{id}.png", img_buffer.read())

print(f"Imágenes guardadas OK !!!")