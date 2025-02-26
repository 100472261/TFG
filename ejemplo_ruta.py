from bearing import calcular_bearing
from latitud_longitud import convertir_latitud_a_decimal, convertir_longitud_a_decimal

#Madrid, España (40° 24’ 59’’ N; 03° 42’ 09’’ O)
#París, Francia (48° 51’ 12’’ N; 02° 20’ 56’’ E)
#Roma, Italia (41° 53’ 30’’ N; 12° 29’ 39’’ E)
#Berlín, Alemania (52° 31’ 28’’ N; 13° 24’ 38’’ E)
#Londres, Inglaterra (51° 30’ 30’’ N; 0° 7’ 32’’ O)

madrid = ["Madrid", [(40, 24, 59, 'N'), (3, 42, 9, 'O')]]
paris = ["París", [(48, 51, 12, 'N'), (2, 20, 56, 'E')]]
roma = ["Roma", [(41, 53, 30, 'N'), (12, 29, 39, 'E')]]
berlin = ["Berlín", [(52, 31, 28, 'N'), (13, 24, 38, 'E')]]
londres = ["Londres", [(51, 30, 30, 'N'), (0, 7, 32, 'O')]]

ruta = [madrid, paris, roma, berlin, londres]
ruta_GD = []
trayectoria = []

for ciudad in ruta:
    nombre = ciudad[0]
    lat = ciudad[1][0]
    lon = ciudad[1][1]
    latitud = convertir_latitud_a_decimal(lat[0], lat[1], lat[2], lat[3])
    longitud = convertir_longitud_a_decimal(lon[0], lon[1], lon[2], lon[3])
    print(f"{nombre} -> GMS: {ciudad[1]} Latitud: {latitud} Longitud: {longitud}")
    ruta_GD.append((latitud, longitud))

for i in range(len(ruta_GD) - 1):
    p1 = ruta_GD[i]
    p2 = ruta_GD[i + 1]
    bearing = calcular_bearing(p1, p2)
    trayectoria.append(bearing)

print("Ángulos ->",trayectoria)