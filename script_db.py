import sqlite3

def crear_base_datos():
    # Creamos la conexión (se guardará en tu carpeta de OneDrive)
    conexion = sqlite3.connect('domovida.db')
    cursor = conexion.cursor()

    print("Creando tablas para DomoVida...")

    # 1. Tabla de Usuarios (Adultos mayores)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER,
        contacto_emergencia TEXT
    )
    ''')

    # 2. Tabla de Sensores
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensores (
        id_sensor TEXT PRIMARY KEY,
        tipo TEXT NOT NULL, -- Ej: Movimiento, Caída, Humedad
        ubicacion TEXT      -- Ej: Habitacion, Baño
    )
    ''')

    # 3. Tabla de Eventos (Aquí caerán los datos de los sensores)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS eventos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_sensor TEXT,
        valor REAL,         -- El dato que envía el sensor
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_sensor) REFERENCES sensores (id_sensor)
    )
    ''')

    conexion.commit()
    conexion.close()
    print("¡Base de datos y tablas configuradas con éxito!")

if __name__ == "__main__":
    crear_base_datos()
    