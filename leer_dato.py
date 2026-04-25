import sqlite3

# Conectamos
conexion = sqlite3.connect('domovida_datos.db')
cursor = conexion.cursor()

# Pedimos ver todo lo que hay en la tabla de signos vitales
cursor.execute("SELECT * FROM signos_vitales")
resultados = cursor.fetchall()

print("--- REGISTROS EN DOMOVIDA ---")
for fila in resultados:
    print(f"ID: {fila[0]} | Fecha: {fila[1]} | Sensor: {fila[2]} | Valor: {fila[3]}")

conexion.close()
