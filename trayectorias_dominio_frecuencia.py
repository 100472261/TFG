import os
import zipfile
import numpy as np
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft

def representacion_dominio_frecuencia(id, xf_filtered, amplitudes_filtered):
    plt.figure(figsize=(6, 6))
    plt.scatter(xf_filtered, amplitudes_filtered, color="k", label="Amplitudes")
    plt.vlines(xf_filtered, ymin=0, ymax=amplitudes_filtered, color="k", linestyle="-")
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    plt.close()
    img_buffer.seek(0)
    zipf.writestr(f"Frecuencia_{id}.png", img_buffer.read())

if __name__ == "__main__":

    #df_path = "./Trayectorias/Tipos_de_barcos/Cargo_modificado_compressed.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/Container_modificado_compressed.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/Cruise_modificado_compressed.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/Fishing_modificado_compressed.csv"
    df_path = "./Trayectorias/Tipos_de_barcos/Tanker_modificado_compressed.csv"

    df = pd.read_csv(df_path)

    trajectory_ids = df['Trajectory_ID'].unique()

    img_dir = "./Imagenes/Trayectorias_dominio_frecuencia"
    os.makedirs(img_dir, exist_ok=True)

    #zip_filename = os.path.join(img_dir, "Frequenzy_Cargo.zip")
    #zip_filename = os.path.join(img_dir, "Frequenzy_Container.zip")
    #zip_filename = os.path.join(img_dir, "Frequenzy_Cruise.zip")
    #zip_filename = os.path.join(img_dir, "Frequenzy_Fishing.zip")
    zip_filename = os.path.join(img_dir, "Frequenzy_Tanker.zip")

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for id in trajectory_ids:
            angulos_ruta = df[df['Trajectory_ID'] == id]['Bearing'].dropna().round(4).tolist()

            N = len(angulos_ruta)
            T = 1
            yf_original = fft(angulos_ruta)
            yf = yf_original[1:N//2]
            xf_original = fftfreq(N, T)[:N//2]
            xf = xf_original[1:]
            amplitudes = 2.0 / N * np.abs(yf)
            xf_filtered = xf[amplitudes > 1]
            amplitudes_filtered = amplitudes[amplitudes > 1]
            
            representacion_dominio_frecuencia(id, xf_filtered, amplitudes_filtered)

            #Reconstrucción de la señal
            #signal_reconstructed = ifft(yf_original * N / 2)
            #plt.figure(figsize=(6, 6))
            #plt.plot(range(len(signal_reconstructed)), np.real(signal_reconstructed), linestyle="-", color="b")
            #plt.show()

    print(f"Trayectorias en el dominio de la frecuencia guardadas OK !!!")
