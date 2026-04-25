# Esto es un diccionario (representa un dato JSON)
dato_sensor = {
    "paciente": "Andres Vergara",
    "sensor": "Frecuencia Cardíaca",
    "valor": 75,
    "unidad": "bpm"
}

# Solo vamos a imprimir el valor para ver si funciona
print("El paciente", dato_sensor["paciente"], "tiene:", dato_sensor["valor"], dato_sensor["unidad"])