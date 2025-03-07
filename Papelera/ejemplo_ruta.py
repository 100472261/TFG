import numpy as np
from bearing import calcular_bearing
from latitud_longitud import convertir_latitud_a_decimal, convertir_longitud_a_decimal

#Madrid, España (40° 24’ 59’’ N; 03° 42’ 09’’ O)
#París, Francia (48° 51’ 12’’ N; 02° 20’ 56’’ E)
#Roma, Italia (41° 53’ 30’’ N; 12° 29’ 39’’ E)
#Berlín, Alemania (52° 31’ 28’’ N; 13° 24’ 38’’ E)
#Londres, Inglaterra (51° 30’ 30’’ N; 0° 7’ 32’’ O)
#Washington DC, Estados Unidos (38º 53’ 42’’ N; 77º 2’ 11’’ O)
#Ciudad de México, México (19° 25’ 42’’ N; 99° 07’ 40’’ O)
#Buenos Aires, Argentina (34° 36’ 47’’ S; 58° 22’ 38’’ O)
#Hong Kong, China (22° 15’ 00’’ N; 114° 10’ 00’’ E)
#Nueva Delhi, India (28° 38’ 8’’ N; 77° 13’ 48’’ E)
#El Cairo, Egipto (30° 03’ 45’’ N; 31° 14’ 59’’ E)

def ejemplo():
    madrid = ["Madrid", [(40, 24, 59, 'N'), (3, 42, 9, 'O')]]
    paris = ["París", [(48, 51, 12, 'N'), (2, 20, 56, 'E')]]
    roma = ["Roma", [(41, 53, 30, 'N'), (12, 29, 39, 'E')]]
    berlin = ["Berlín", [(52, 31, 28, 'N'), (13, 24, 38, 'E')]]
    londres = ["Londres", [(51, 30, 30, 'N'), (0, 7, 32, 'O')]]
    washington = ["Washington DC", [(38, 53, 42, 'N'), (77, 2, 11, 'O')]]
    mexico = ["Ciudad de México", [(19, 25, 42, 'N'), (99, 7, 40, 'O')]]
    buenos_aires = ["Buenos Aires", [(34, 36, 47, 'S'), (58, 22, 38, 'O')]]
    hong_kong = ["Hong Kong", [(22, 15, 0, 'N'), (114, 10, 0, 'E')]]
    nueva_delhi = ["Nueva Delhi", [(28, 38, 8, 'N'), (77, 13, 48, 'E')]]
    el_cairo = ["El Cairo", [(30, 3, 45, 'N'), (31, 14, 59, 'E')]]

    ruta = [madrid, paris, roma, berlin, londres, washington, mexico, buenos_aires, hong_kong, nueva_delhi, el_cairo]
    ruta_GD = []
    angulos_ruta = []
    lista_latitudes = []
    lista_longitudes = []

    for ciudad in ruta:
        nombre = ciudad[0]
        lat = ciudad[1][0]
        lon = ciudad[1][1]
        latitud = convertir_latitud_a_decimal(lat[0], lat[1], lat[2], lat[3])
        lista_latitudes.append(latitud)
        longitud = convertir_longitud_a_decimal(lon[0], lon[1], lon[2], lon[3])
        lista_longitudes.append(longitud)
        #print(f"{nombre} -> GMS: {ciudad[1]} Latitud: {latitud} Longitud: {longitud}")
        ruta_GD.append((latitud, longitud))

    for i in range(len(ruta_GD) - 1):
        p1 = ruta_GD[i]
        p2 = ruta_GD[i + 1]
        bearing = calcular_bearing(p1, p2)
        angulos_ruta.append(round(bearing, 3))

    lista_latitudes = np.array(lista_latitudes)
    lista_longitudes = np.array(lista_longitudes)
    angulos_ruta = np.array(angulos_ruta)

    return lista_latitudes, lista_longitudes, angulos_ruta

if __name__ == "__main__":
    lista_latitudes, lista_longitudes, angulos_ruta = ejemplo()
    print("Latitudes ->",lista_latitudes)
    print("Longitudes ->",lista_longitudes)
    print("Ángulos ->",angulos_ruta)
