import sqlite3

class EstudianteModel:
    def insertar(self, nombre, edad, carrera):
        conexion = sqlite3.connect("estudiantes.db")
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO estudiantes(nombre, edad, carrera) VALUES (?, ?, ?)",
            (nombre, edad, carrera)
        )

        conexion.commit()
        conexion.close()

    def mostrar(self):
        conexion = sqlite3.connect("estudiantes.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM estudiantes")
        datos = cursor.fetchall()

        conexion.close()
        return datos

    def actualizar(self, id_estudiante, nombre, edad, carrera):
        conexion = sqlite3.connect("estudiantes.db")
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE estudiantes
            SET nombre=?, edad=?, carrera=?
            WHERE id=?
        """, (nombre, edad, carrera, id_estudiante))

        conexion.commit()
        conexion.close()

    def eliminar(self, id_estudiante):
     conexion = sqlite3.connect("estudiantes.db")
     cursor = conexion.cursor()

     cursor.execute(
        "DELETE FROM estudiantes WHERE id=?",
        (id_estudiante,)
       )

     conexion.commit()
     conexion.close()