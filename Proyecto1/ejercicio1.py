class Persona:

    def inicializar(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def imprimir(self):
        print("Nombre",self.nombre)
        print("Edad",self.edad)

    def mayor_edad(self):
        if self.edad>=18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")


# bloque principal

persona1=Persona()
persona1.inicializar("Antonio",18)
persona1.imprimir()
persona1.mayor_edad()

