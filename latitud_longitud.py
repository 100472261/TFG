def convertir_latitud_a_decimal(grados, minutos, segundos, direccion):
    decimal = grados + minutos / 60 + segundos / 3600
    if direccion == 'S':
        decimal = -decimal
    return decimal

def convertir_latitud_a_GMS(decimal):
    if decimal < 0:
        direccion = "S"
    else:
        direccion = "N"
    decimal = abs(decimal)
    grados = int(decimal)
    minutos = int((decimal - grados) * 60)
    segundos = (decimal - grados - minutos / 60) * 3600
    return grados, minutos, segundos, direccion

def convertir_longitud_a_decimal(grados, minutos, segundos, direccion):
    decimal = grados + minutos / 60 + segundos / 3600
    if direccion == 'O':
        decimal = -decimal
    return decimal

def convertir_longitud_a_GMS(decimal):
    if decimal < 0:
        direccion = 'O'
    else:
        direccion = 'E'
    decimal = abs(decimal)
    grados = int(decimal)
    minutos = int((decimal - grados) * 60)
    segundos = (decimal - grados - minutos / 60) * 3600
    return grados, minutos, segundos, direccion

#Madrid (40° 25' 0.049'' N; 3° 42' 12.958'' O)
latitud = convertir_latitud_a_decimal(40, 25, 0.049, 'N')
longitud = convertir_longitud_a_decimal(3, 42, 12.958, 'O')
print(latitud, longitud)
latitud_GMS = convertir_latitud_a_GMS(latitud)
longitud_GMS = convertir_longitud_a_GMS(longitud)
print(f"{latitud_GMS[0]}° {latitud_GMS[1]}' {latitud_GMS[2]:.3f}'' {latitud_GMS[3]}; {longitud_GMS[0]}° {longitud_GMS[1]}' {longitud_GMS[2]:.3f}'' {longitud_GMS[3]}")