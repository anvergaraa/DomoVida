import sqlite3

# 1. Conectamos a la base de datos que ya existe
conexion = sqlite3.connect('domovida_datos.db')
cursor = conexion.cursor()

# 2. Definimos el dato (como el que hicimos antes)
tipo_sensor = "Ritmo Cardíaco"
valor_sensor = 82.5

# 3. Insertamos el dato en la tabla
cursor.execute("INSERT INTO signos_vitales (tipo_sensor, valor) VALUES (?, ?)", 
               (tipo_sensor, valor_sensor))

# 4. Guardamos y cerramos
conexion.commit()
print("¡Dato guardado exitosamente en la base de datos!")
conexion.close()