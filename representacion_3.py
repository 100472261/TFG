import pandas as pd
import matplotlib.pyplot as plt
from ejemplo_ruta import ejemplo

lista_latitudes, lista_longitudes, angulos_ruta = ejemplo()

serie_angulos_ruta = pd.Series(angulos_ruta)
print(serie_angulos_ruta)

plt.plot(range(len(serie_angulos_ruta)), serie_angulos_ruta, marker="o", linestyle="-", color="b", mfc="k")
output_path = "./Imagenes_representacion_3/señal_1.png"
plt.savefig(output_path)
