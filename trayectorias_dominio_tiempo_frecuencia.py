import os
import pywt
import zipfile
import numpy as np
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt

if __name__ == "__main__":

    df_path = "./Trayectorias/Tipos_de_barcos/longitud_28/Tanker_modificado_compressed_28_v4_COMPLETO.csv"

    df = pd.read_csv(df_path)

    trajectory_ids = df['Trajectory_ID'].unique()

    img_dir = "./Imagenes/Trayectorias_dominio_tiempo_frecuencia/longitud_28"
    os.makedirs(img_dir, exist_ok=True)

    #zip_filename = os.path.join(img_dir, "Cargo.zip")
    #zip_filename = os.path.join(img_dir, "Fishing.zip")
    #zip_filename = os.path.join(img_dir, "Military.zip")
    #zip_filename = os.path.join(img_dir, "Sailing.zip")
    zip_filename = os.path.join(img_dir, "Tanker.zip")

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for id in trajectory_ids:
            trajectory_data = df[df['Trajectory_ID'] == id]['Bearing'].dropna().round(4).to_list()

            family = ['morl']

            for wv in family:
                #Escala grande  -> Detecta baja frecuencia (Forma general)
                #Escala pequeña -> Detecta alta frecuencia (Detalles finos)
                scales = np.arange(1, 100)
                coefficients, frequencies = pywt.cwt(trajectory_data, scales, wv)

                plt.figure(figsize=(6, 6))
                
                #plt.subplot(2, 1, 1)
                #plt.plot(trajectory_data)
                #plt.title('Time Domain')
                #plt.xlabel('time [s]')
                #plt.ylabel('Amplitude')

                #plt.subplot(2, 1, 1)
                coef_abs = np.abs(coefficients)
                plt.imshow(coef_abs, extent=[0, len(trajectory_data), 1, 100], cmap='inferno', aspect='auto', vmax=np.percentile(np.abs(coefficients), 99), vmin=np.percentile(np.abs(coefficients), 1))
                #plt.xlabel('time [s]')
                #plt.ylabel('Scale')
                #plt.colorbar(label='Magnitude')
                plt.colorbar()
                #plt.tight_layout()
                
                img_buffer = BytesIO()
                plt.savefig(img_buffer, format="png")
                plt.close()
                img_buffer.seek(0)
                zipf.writestr(f"Trayectoria_dominio_tiempo_frecuencia_{id}.png", img_buffer.read())

    print(f"Trayectorias en el dominio del tiempo y la frecuencia guardadas OK !!!")
