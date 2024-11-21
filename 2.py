#definición de la clase Persona
class Persona:
    #recibe el nombre y la edad al crear una instancia
    def __init__(self, nombre, edad):
    
        self.nombre = nombre
        self.edad = edad

    # Método que simula el cumpleaños de la persona
    def cumpleaños(self):
        self.edad += 1

# Crear una instancia de la clase Persona
p = Persona("Tagle", 16)

# Llamamos al método 'cumpleaños' dos veces para aumentar la edad del individuo
p.cumpleaños() 
p.cumpleaños()  

# Imprimimos el nombre y la edad final después de los dos cumpleaños
print(f"{p.nombre} cumple {p.edad} años")
