class compas:
    def hablar(self):
        return "que royo, soy un indigente"


class pepino(compas):
    def hablar(self):
        return "Hola, soy pepin y soy un chapulin"


class tagle(compas):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        return self.mensaje


# Crear objetos de cada clase
indigente = compas()
pepino = pepino()
tagle = tagle("Hola, soy tagle y me encantan las mujeres")

# Mostrar los mensajes
print(indigente.hablar())  
print(pepino.hablar())    
print(tagle.hablar())        
