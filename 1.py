class Estudiante:
    # constructor de la clase recibe el nombre del estudiante
    def __init__(self, nombre):
        # guarda el nombre del estudiante como un atributo
        self.nombre = nombre
        #  diccionario vacío para almacenar las calificaciones por asignatura
        self.calificaciones = {}

    # permite agregar unna calificacion en cada asignatura
    def agregar_calificacion(self, asignatura, nota):

        self.calificaciones[asignatura] = nota
    # imprime los resultados del estudiante
    def imprimir_resultados(self):

        print(f"Resultados de {self.nombre}:")
  
        for asignatura, nota in self.calificaciones.items():
            # Si la nota es mayor o igual a 6, el estudiante ha aprobado
            resultado = "APROBADO" if nota >= 6 else "REPROBADO"
            # Imprime la asignatura, la calificación y el resultado
            print(f"{asignatura}: Nota = {nota} | Resultado: {resultado}")

# Crear una instancia para el estudiante
estudiante1 = Estudiante("piedra")
#calificaciones para diferentes asignaturas
estudiante1.agregar_calificacion("Matemáticas", 5)
estudiante1.agregar_calificacion("Historia", 8)
# Imprimir los resultados del estudiante
estudiante1.imprimir_resultados()

# Crear una instancia para el estudiante
estudiante2 = Estudiante("pepin")
# calificaciones para diferentes asignaturas
estudiante2.agregar_calificacion("Matemáticas", 7)
estudiante2.agregar_calificacion("Historia", 9)
# Imprimir los resultados del estudiante
estudiante2.imprimir_resultados()

