import sqlite3

def crear_base_nueva():
    conexion = sqlite3.connect('base_domovida.db')
    cursor = conexion.cursor()
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
    print("--- BASE DE DATOS CREADA Y RECONOCIDA ---")

if __name__ == "__main__":
    crear_base_nueva()