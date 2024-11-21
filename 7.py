class Universidad:
    def __init__(self, nombre_universidad):
        self.nombre_universidad = nombre_universidad


class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad


class Estudiante:
    def __init__(self, nombre, edad, universidad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad
        self.carrera = carrera

    def mostrar_informacion(self):
        return (f"Nombre: {self.nombre}\n"
                f"Edad: {self.edad}\n"
                f"Universidad: {self.universidad.nombre_universidad}\n"
                f"Especialidad: {self.carrera.especialidad}")


# Crear objetos
universidad = Universidad(nombre_universidad="UACEjota")
carrera = Carrera(especialidad="Quimico Farmacobiologia")
persona = Estudiante(nombre="Frias Angel Valentin", edad=20, universidad=universidad, carrera=carrera)

# Mostrar la información del estudiante
print(persona.mostrar_informacion())
