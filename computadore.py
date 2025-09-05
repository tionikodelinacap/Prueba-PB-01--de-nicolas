#importa clases
from dispositivo import Dispositivo
#se crea clase hija (herencia)
class Computadora(Dispositivo):
    def __init__(self, marca, modelo, precio, ram):
        super().__init__(marca, modelo, precio)
        self.ram = ram
    
    # se sobreescribe el motodo descripcion(polimorfismo)
    def descripcion(self):
        return f"la marca del Computador es: {self.marca} y tiene {self.ram} de ram"
    
    
