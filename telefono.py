#importa clases
from dispositivo import Dispositivo
#se crea clase hijo(herencia)
class Telefono(Dispositivo):
    def __init__(self, marca, modelo, precio, camara):
        super().__init__(marca, modelo, precio)
        self.camara = camara
        
    # se sobreescribe el motodo descripcion(polimorfismo)
    def descripcion(self):
        return f"la marca del Telefono/celular es: {self.marca} y tiene una camara de {self.camara} megapixeles"