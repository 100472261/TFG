import os
import pandas as pd
import numpy as np
import pywt
import matplotlib.pyplot as plt

if __name__ == "__main__":

    df_path = "./Wavelets_pruebas/ECG.xlsx"
    df = pd.read_excel(df_path)
    trajectory_data = df[51].dropna().to_numpy()

    family = ['mexh', 'morl']

    for wv in family:
        #Escala grande  -> Detecta baja frecuencia (Forma general)
        #Escala pequeña -> Detecta alta frecuencia (Detalles finos)
        scales = np.arange(1, 100)
        coefficients, frequencies = pywt.cwt(trajectory_data, scales, wv)

        plt.figure(figsize=(15, 10))
        plt.subplot(2, 1, 1)
        plt.plot(trajectory_data)
        plt.title('Time Domain')
        plt.xlabel('time [s]')
        plt.ylabel('Amplitude')

        plt.subplot(2, 1, 2)
        coef_abs = np.abs(coefficients)
        plt.imshow(coef_abs, extent=[0, len(trajectory_data), 1, 100], cmap='inferno', aspect='auto', vmax=np.percentile(np.abs(coefficients), 99), vmin=np.percentile(np.abs(coefficients), 1))
        plt.title('Time-Frequency Domain')
        plt.xlabel('time [s]')
        plt.ylabel('Scale')
        plt.colorbar(label='Magnitude')
        plt.tight_layout()

        img_dir = "./Wavelets_pruebas"
        plt.savefig(f"{img_dir}/Ejemplo_{wv}.png")

    print(f"Trayectorias en el dominio del tiempo y la frecuencia guardadas OK !!!")
