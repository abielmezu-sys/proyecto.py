import tkinter as tk
from tkinter import ttk

class EstudianteView:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="#dbeafe")
        self.root.title("Sistema de Gestión de Estudiantes")
        self.root.geometry("1200x700")
        self.root.resizable(True, True)

        titulo = tk.Label(
            root,
            text="Sistema de Gestión de Estudiantes",
            font=("Arial", 18, "bold"),
            bg="#dbeafe"
        )
        titulo.pack(pady=10)
        self.root.state("zoomed")
        self.root.title("Sistema de Gestión de Estudiantes")
        self.root.state("zoomed")
        self.root.config(bg="#dbeafe")

        tk.Label(
        root,
        text="Nombre",
        bg="#dbeafe",
        font=("Arial", 11)
        ).pack(pady=5)

        self.nombre = tk.Entry(
        root,
        width=40,
        font=("Arial", 11)
           )
        self.nombre.pack()

        tk.Label(
        root,
        text="Edad",
        bg="#dbeafe",
        font=("Arial", 11)
         ).pack(pady=5)

        self.edad = tk.Entry(
        root,
        width=40,
        font=("Arial", 11)
     )
        self.edad.pack()

        tk.Label(
        root,
        text="Carrera",
        bg="#dbeafe",
        font=("Arial", 11)
          ).pack(pady=5)

        self.carrera = tk.Entry(
        root,
        width=40,
        font=("Arial", 11)
         )
        self.carrera.pack()
        self.btn_guardar = tk.Button(root, text="Guardar")
        self.btn_actualizar = tk.Button(root, text="Actualizar")
        self.btn_actualizar.pack()

        self.btn_eliminar = tk.Button(root, text="Eliminar")
        self.btn_eliminar.pack()
        self.btn_guardar.pack()


        self.tabla = ttk.Treeview(
            root,
            columns=("ID", "Nombre", "Edad", "Carrera"),
            show="headings"
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Edad", text="Edad")
        self.tabla.heading("Carrera", text="Carrera")

        self.tabla.pack(fill="both", expand=True)