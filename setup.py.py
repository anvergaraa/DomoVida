import sqlite3

def crear_base():
    # Esto crea el archivo físico si no existe
    conexion = sqlite3.connect('domovida_datos.db')
    cursor = conexion.cursor()
    
    # Esto crea la tabla donde se guardarán los latidos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS signos_vitales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_sensor TEXT,
            valor REAL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conexion.commit()
    conexion.close()
    print("✅ BASE DE DATOS RECONOCIDA Y TABLA CREADA CON ÉXITO")

if __name__ == "__main__":
    crear_base()