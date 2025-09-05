#importa clases
from dispositivo import Dispositivo
#se crea clase hija(herencia)
class Tablet(Dispositivo):
    def __init__(self, marca, modelo, precio, pulgadas):
        super().__init__(marca, modelo, precio)
        self.pulgadas = pulgadas
        
    # se sobreescribe el motodo descripcion(polimorfismo)
    def descripcion(self):
        return f"la marca de tablet es: {self.marca} y la pantalla es de {self.pulgadas} pulgadas"