import numpy as np

def calcular_bearing(p1, p2):

    lat1, lon1 = p1[0], p1[1]
    lat2, lon2 = p2[0], p2[1]

    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    y = np.sin(lon2 - lon1) * np.cos(lat2)
    x1 = np.cos(lat1) * np.sin(lat2)
    x2 = np.sin(lat1) * np.cos(lat2) * np.cos(lon2 - lon1)

    bearing = np.degrees(np.arctan2(y, (x1 - x2)))

    bearing = (bearing + 360) % 360

    return bearing
