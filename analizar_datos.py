import sqlite3

conexion = sqlite3.connect('domovida_datos.db')
cursor = conexion.cursor()

# Pedimos el promedio, el valor máximo y el total de registros
cursor.execute("SELECT AVG(valor), MAX(valor), COUNT(*) FROM signos_vitales")
resultado = cursor.fetchone()

print("--- REPORTE DE SALUD DOMOVIDA ---")
print(f"Total de mediciones: {resultado[2]}")
print(f"Ritmo Cardíaco Promedio: {resultado[0]:.2f} bpm")
print(f"Ritmo Cardíaco Máximo: {resultado[1]} bpm")

conexion.close()