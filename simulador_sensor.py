import sqlite3
import random
import time

def simular():
    conexion = sqlite3.connect('base_domovida.db')
    cursor = conexion.cursor()
    print("--- Iniciando Simulación de Sensor ---")
    
    try:
        while True:
            ritmo = random.randint(60, 100)
            # Insertamos solo el número en 'valor'
            cursor.execute("INSERT INTO signos_vitales (tipo_sensor, valor) VALUES (?, ?)", 
                           ("Ritmo Cardíaco", ritmo))
            conexion.commit()
            print(f"Dato enviado: {ritmo} bpm")
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nSimulación detenida.")
    finally:
        conexion.close()

if __name__ == "__main__":
    simular()
