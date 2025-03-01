import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ejemplo_ruta import ejemplo
from scipy.fftpack import fft, fftfreq, ifft

# Definir la señal en el tiempo (datos proporcionados)
signal_time = np.array([24.949, 130.614, 3.018, 268.422, 288.445, 230.749, 144.134, 150.194,
                        288.641, 283.676] * 5)  # Repetida para hacerla más clara

N = len(signal_time)  # Número de muestras
T = 1  # Intervalo de muestreo (asumimos que es uniforme)
t = np.linspace(0, N, N)  # Vector de tiempo

# Aplicar la FFT a la señal
yf = fft(signal_time)
xf = fftfreq(N, T)[:N // 2]  # Solo frecuencias positivas

# Obtener amplitudes de las frecuencias
amplitudes_fft = 2.0 / N * np.abs(yf[:N // 2])

# Filtrar las frecuencias con mayor contribución (umbral del 10% del máximo)
umbral = np.max(amplitudes_fft) * 0.1
frecuencias_significativas = xf[amplitudes_fft > umbral]
amplitudes_significativas = amplitudes_fft[amplitudes_fft > umbral]

# Graficar las frecuencias detectadas
plt.figure(figsize=(6, 6))
plt.scatter(frecuencias_significativas, amplitudes_significativas, color="r", label="Frecuencias dominantes")
plt.vlines(frecuencias_significativas, ymin=0, ymax=amplitudes_significativas, color="r", linestyle="dashed")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.title("Frecuencias Dominantes en la Señal")
plt.legend()
plt.grid()
plt.show()

# Reconstrucción de la señal a partir de las frecuencias dominantes
t_reconstruccion = np.linspace(0, N, 500)  # Más puntos para suavizar la señal
signal_reconstructed_filtered = sum(A * np.sin(2 * np.pi * f * t_reconstruccion) for A, f in zip(amplitudes_significativas, frecuencias_significativas))

# Graficar la señal original y las componentes sinusoidales sin la señal reconstruida

# Ajustar la fase inicial y centrar las ondas en 24.949
valor_inicial = signal_time[0]  # Primer valor de la señal original
fases = np.arcsin(valor_inicial / amplitudes_significativas)  # Calcular fase para cada frecuencia

# Graficar la señal original en negro
plt.figure(figsize=(10, 6))
plt.plot(t, signal_time, color="black", linewidth=2, label="Señal Original")

# Graficar cada onda sinusoidal individualmente, centrada en 24.949
for i, (A, f, phi) in enumerate(zip(amplitudes_significativas, frecuencias_significativas, fases)):
    wave = A * np.sin(2 * np.pi * f * t_reconstruccion + phi) + valor_inicial  # Aplicar fase y centrar en 24.949
    plt.plot(t_reconstruccion, wave, linestyle="--", label=f"Onda {i+1}: Frec={round(f, 2)} Hz, Amp={round(A, 2)}")

# Etiquetas y título
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.title("Señal Original y sus Componentes Sinusoidales (Ajustadas en Fase y Centrada)")
plt.legend()
plt.grid()

# Mostrar la gráfica
plt.show()
