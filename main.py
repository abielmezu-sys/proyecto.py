# Importamos tkinter para crear la ventana principal
import tkinter as tk

# Importamos el archivo de base de datos
# Aquí está la función que crea la tabla
import database

# Importamos la vista
# Se encarga de la interfaz gráfica
from estudiante_view import EstudianteView

# Importamos el controlador
# Conecta la vista con el modelo
from estudiante_controller import EstudianteController


# Ejecutamos la función que crea la base de datos
# Esto asegura que la tabla exista antes de iniciar
database.crear_bd()


# Creamos la ventana principal
root = tk.Tk()

# Creamos la vista y le pasamos la ventana
vista = EstudianteView(root)

# Creamos el controlador y le pasamos la vista
controlador = EstudianteController(vista)

# Iniciamos el ciclo principal de la interfaz
# Mantiene la ventana abierta
root.mainloop()