
# se declaran todas las funciones 
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Error: División por cero"

#solicita al usuario ingresar dos números enteros
numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))

# crea una instancia de la clase Calculadora
calculadora = Calculadora(numero1, numero2)

# Realizar e imprimir las operaciones
print(f"Suma: {calculadora.sumar()}")
print(f"Resta: {calculadora.restar()}")
print(f"Multiplicación: {calculadora.multiplicar()}")
print(f"División: {calculadora.dividir()}")
