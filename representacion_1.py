import numpy as np
from ejemplo_ruta import ejemplo

lista_latitudes, lista_longitudes, angulos_ruta = ejemplo()
angulos_ruta_ampliada = []
for i in range(5):
    for i in angulos_ruta:
        angulos_ruta_ampliada.append(i)
angulos_ruta_ampliada = np.array(angulos_ruta_ampliada)
print(angulos_ruta_ampliada)
