import os
import zipfile
import numpy as np
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft

def reconstruccion_señal():
    t = np.arange(N)
    señal = np.zeros(N)
    for i in range(N):
        señal += amplitudes[i] * np.cos(2 * np.pi * xf[i] * t + phases[i])
    plt.figure(figsize=(12, 6))
    plt.plot(angulos_ruta, 'o-', label="Señal original")
    plt.plot(señal, 'x-', label="Señal reconstruida", linestyle="--")
    plt.legend()
    plt.grid(True)
    plt.show()

def representacion_dominio_frecuencia(id, xf_filtered, amplitudes_filtered):
    plt.figure(figsize=(12, 6))
    plt.scatter(xf_filtered, amplitudes_filtered, color="k", label="Amplitudes")
    plt.vlines(xf_filtered, ymin=0, ymax=amplitudes_filtered, color="k", linestyle="-")
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    plt.close()
    img_buffer.seek(0)
    zipf.writestr(f"Frequency_{id}.png", img_buffer.read())

if __name__ == "__main__":

    df_path = "./Trayectorias/Tipos_de_barcos/longitud_28/Cargo_modificado_compressed_28_v3_COMPLETO.csv"

    df = pd.read_csv(df_path)

    trajectory_ids = df['Trajectory_ID'].unique()

    trajectory_ids = [6]

    img_dir = "./Imagenes"
    os.makedirs(img_dir, exist_ok=True)

    zip_filename = os.path.join(img_dir, "Frequency_Cargo.zip")
    #zip_filename = os.path.join(img_dir, "Frequency_Container.zip")
    #zip_filename = os.path.join(img_dir, "Frequency_Cruise.zip")
    #zip_filename = os.path.join(img_dir, "Frequency_Fishing.zip")
    #zip_filename = os.path.join(img_dir, "Frequency_Tanker.zip")

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for id in trajectory_ids:
            angulos_ruta = df[df['Trajectory_ID'] == id]['Bearing'].dropna().round(4).tolist()

            N = len(angulos_ruta)
            T = 1
            yf = fft(angulos_ruta)
            xf = fftfreq(N, T)[:N]
            amplitudes = np.abs(yf) / N
            phases = np.angle(yf)

            print("Amplitudes: ", amplitudes)
            print("Frecuencias: ", xf)
            
            reconstruccion_señal()
                
            representacion_dominio_frecuencia(id, xf, amplitudes)

    print(f"Trayectorias en el dominio de la frecuencia guardadas OK !!!")
