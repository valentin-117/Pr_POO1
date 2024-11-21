class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido) 
        self.edad = edad
        self.carrera = carrera

    def mostrar_carrera(self):
        return f"Estudia la carrera de {self.carrera}."


# datos del usuario
nombre = input("Ingrese el nombre del estudiante: ")
apellido = input("Ingrese el apellido del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
carrera = input("Ingrese la carrera del estudiante: ")

# Crear instancia de Estudiante
estudiante = Estudiante(nombre, apellido, edad, carrera)

# Mostrar información en orden
print("\nInformación del Estudiante:")
print(f"Nombre completo: {estudiante.nombre_completo()}")
print(f"Edad: {estudiante.edad}")
print(estudiante.mostrar_carrera())
