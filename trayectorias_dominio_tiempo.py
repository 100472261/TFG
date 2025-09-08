import os
import zipfile
import numpy as np
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def representar_trayectoria_bearing(angulos_ruta, id):
    plt.figure(figsize=(12, 6))
    plt.plot(angulos_ruta, color="k", label="Bearing", lw=3)

    # plt.xticks([])
    # plt.yticks([])

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    plt.close()
    img_buffer.seek(0)
    zipf.writestr(f"Trayectoria_dominio_tiempo_{id}.png", img_buffer.read())


if __name__ == "__main__":

    df_path = "./Trayectorias/Tipos_de_barcos/v2/Cargo_modificado_v2.csv"

    df = pd.read_csv(df_path)

    trajectory_ids = df['Trajectory_ID'].unique()

    trajectory_ids = [3]  # Puedes cambiar esto para probar con otros IDs

    img_dir = "./Papelera"
    os.makedirs(img_dir, exist_ok=True)

    zip_filename = os.path.join(img_dir, "3.zip")
    #zip_filename = os.path.join(img_dir, "Container.zip")
    #zip_filename = os.path.join(img_dir, "Cruise.zip")
    #zip_filename = os.path.join(img_dir, "Fishing.zip")
    #zip_filename = os.path.join(img_dir, "Tanker.zip")

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for id in trajectory_ids:
            angulos_ruta = df[df['Trajectory_ID'] == id]['Bearing'].dropna().round(4).tolist()
            scaler = MinMaxScaler()
            angulos_ruta = scaler.fit_transform(np.array(angulos_ruta).reshape(-1, 1)).flatten()
            representar_trayectoria_bearing(angulos_ruta, id)

    print(f"Trayectorias en el dominio del tiempo guardadas OK !!!")