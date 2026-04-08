import sqlite3

def crear_bd():
    conexion = sqlite3.connect("estudiantes.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            carrera TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()