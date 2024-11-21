class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_atributos(self):
        return f"Llantas: {self.llantas}, Color: {self.color}, Precio: ${self.precio}"


class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=2, color=color, precio=precio)  # Las motos tienen 2 llantas


class Carro(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=4, color=color, precio=precio)  # Los carros tienen 4 llantas


# Crear objetos de las clases
moto = Moto(color="Rojo", precio=23.590)
carro = Carro(color="Azul", precio=20.000)

# Mostrar atributos de cada objeto
print("Moto:")
print(moto.mostrar_atributos())

print("\nCarro:")
print(carro.mostrar_atributos())
