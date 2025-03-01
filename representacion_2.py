import matplotlib.pyplot as plt
from ejemplo_ruta import ejemplo

lista_latitudes, lista_longitudes, angulos_ruta = ejemplo()

lat_min, lat_max = min(lista_latitudes), max(lista_latitudes)
lon_min, lon_max = min(lista_longitudes), max(lista_longitudes)

def normalizar(value, min_val, max_val, new_min, new_max):
    return int((value - min_val) / (max_val - min_val) * (new_max - new_min) + new_min)

coordenadas_pix = []

for lat, lon in zip(lista_latitudes, lista_longitudes):
    coordenadas_pix.append((normalizar(lat, lat_min, lat_max, 0, 99), normalizar(lon, lon_min, lon_max, 0, 99)))

coordenadas_y, coordenadas_x = zip(*coordenadas_pix)

plt.figure(figsize=(6, 6))
plt.plot(coordenadas_x, coordenadas_y, marker="o", linestyle="-", color="b", mfc="k")
output_path = "./Imagenes_representacion_2/trayectoria_1.png"
plt.savefig(output_path)
