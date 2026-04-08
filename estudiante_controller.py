from estudiante_model import EstudianteModel

class EstudianteController:
    def __init__(self, view):
        self.view = view
        self.model = EstudianteModel()

        self.view.btn_guardar.config(command=self.guardar)
        self.view.btn_actualizar.config(command=self.actualizar)
        self.view.btn_eliminar.config(command=self.eliminar)

        self.cargar_datos()

    def guardar(self):
        nombre = self.view.nombre.get()
        edad = self.view.edad.get()
        carrera = self.view.carrera.get()

        self.model.insertar(nombre, edad, carrera)
        self.cargar_datos()

    def cargar_datos(self):
        for fila in self.view.tabla.get_children():
            self.view.tabla.delete(fila)

        datos = self.model.mostrar()

        for dato in datos:
            self.view.tabla.insert("", "end", values=dato)

    def actualizar(self):
        seleccionado = self.view.tabla.selection()[0]
        datos = self.view.tabla.item(seleccionado)["values"]

        self.model.actualizar(
            datos[0],
            self.view.nombre.get(),
            self.view.edad.get(),
            self.view.carrera.get()
        )

        self.cargar_datos()

    def eliminar(self):
     seleccion = self.view.tabla.selection()

     if not seleccion:
        print("Selecciona un estudiante para eliminar")
        return

     item = seleccion[0]
     datos = self.view.tabla.item(item)["values"]

     self.model.eliminar(datos[0])
     self.cargar_datos()