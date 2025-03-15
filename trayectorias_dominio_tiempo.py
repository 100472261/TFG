import os
import zipfile
import numpy as np
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def representar_trayectoria_bearing(angulos_ruta, id):
    plt.figure(figsize=(6, 6))
    plt.plot(angulos_ruta, color="k", label="Bearing")
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    plt.close()
    img_buffer.seek(0)
    zipf.writestr(f"Bearing_{id}.png", img_buffer.read())



if __name__ == "__main__":

    #df_path = "./Trayectorias/Tipos_de_barcos/Cargo_modificado_compressed.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/Container_modificado_compressed.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/Cruise_modificado_compressed.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/Fishing_modificado_compressed.csv"
    df_path = "./Trayectorias/Tipos_de_barcos/Tanker_modificado_compressed.csv"

    df = pd.read_csv(df_path)

    trajectory_ids = df['Trajectory_ID'].unique()

    img_dir = "./Imagenes/Trayectorias_dominio_tiempo"
    os.makedirs(img_dir, exist_ok=True)

    #zip_filename = os.path.join(img_dir, "Bearing_Cargo.zip")
    #zip_filename = os.path.join(img_dir, "Bearing_Container.zip")
    #zip_filename = os.path.join(img_dir, "Bearing_Cruise.zip")
    #zip_filename = os.path.join(img_dir, "Bearing_Fishing.zip")
    zip_filename = os.path.join(img_dir, "Bearing_Tanker.zip")

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for id in trajectory_ids:
            angulos_ruta = df[df['Trajectory_ID'] == id]['Bearing'].dropna().round(4).tolist()
            scaler = MinMaxScaler()
            angulos_ruta = scaler.fit_transform(np.array(angulos_ruta).reshape(-1, 1)).flatten()
            representar_trayectoria_bearing(angulos_ruta, id)

    print(f"Trayectorias en el dominio del tiempo guardadas OK !!!")