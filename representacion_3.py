import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Papelera.ejemplo_ruta import ejemplo
from scipy.fftpack import fft, fftfreq, ifft

lista_latitudes, lista_longitudes, angulos_ruta = ejemplo()
angulos_ruta_ampliada = []
for i in range(5):
    for i in angulos_ruta:
        angulos_ruta_ampliada.append(i)
angulos_ruta_ampliada = np.array(angulos_ruta_ampliada)

serie_angulos_ruta = pd.Series(angulos_ruta_ampliada)

#Representación en el dominio del tiempo
plt.figure(figsize=(6, 6))
plt.plot(range(len(serie_angulos_ruta)), serie_angulos_ruta, linestyle="-", color="b", mfc="k")
output_path = "./Imagenes_representacion_3/señal_1.png"
plt.savefig(output_path)

angulos_ruta = serie_angulos_ruta.to_numpy()

N = len(angulos_ruta)
T = 1
yf_original = fft(angulos_ruta)
yf = yf_original[1:N//2]
xf_original = fftfreq(N, T)[:N//2]
xf = xf_original[1:]
amplitudes = 2.0 / N * np.abs(yf)
xf_filtered = xf[amplitudes > 1]
amplitudes_filtered = amplitudes[amplitudes > 1]

#Representación en el dominio de la frecuencia
plt.figure(figsize=(6, 6))
plt.scatter(xf_filtered, amplitudes_filtered, color="r", label="Amplitudes")
plt.vlines(xf_filtered, ymin=0, ymax=amplitudes_filtered, color="r", linestyle="-")
output_path = "./Imagenes_representacion_3/frecuencia_1.png"
plt.savefig(output_path)

#Señal reconstruida
#signal_reconstructed = ifft(yf_original * N / 2)
#plt.figure(figsize=(6, 6))
#plt.plot(range(len(signal_reconstructed)), np.real(signal_reconstructed), linestyle="-", color="b")
#output_path = "./Imagenes_representacion_3/señal_rec_1.png"
#plt.savefig(output_path)
