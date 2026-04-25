import sqlite3

# 1. Creamos la conexión (esto crea un archivo llamado domovida_datos.db)
conexion = sqlite3.connect('domovida_datos.db')
cursor = conexion.cursor()

# 2. Creamos una tabla para guardar los signos vitales
cursor.execute('''
    CREATE TABLE IF NOT EXISTS signos_vitales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
        tipo_sensor TEXT,
        valor REAL
    )
''')

print("¡Base de datos de DomoVida creada con éxito!")

conexion.commit()
conexion.close()
