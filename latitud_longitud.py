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
