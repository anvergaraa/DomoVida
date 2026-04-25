import sqlite3

conexion = sqlite3.connect('domovida_datos.db')
cursor = conexion.cursor()

# Borramos todos los registros de la tabla
cursor.execute("DELETE FROM signos_vitales")
conexion.commit()

print("¡Base de datos vaciada con éxito! Lista para nuevas pruebas.")
conexion.close()