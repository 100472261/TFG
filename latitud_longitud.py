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

latitud = convertir_latitud_a_GMS(35.262650)
longitud = convertir_longitud_a_GMS(-59.453625)
print(f"{latitud[0]}°{latitud[1]}'{latitud[2]:.2f}\"{latitud[3]} {longitud[0]}°{longitud[1]}'{longitud[2]:.2f}\"{longitud[3]}")