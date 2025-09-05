#importa clases
from dispositivo import Dispositivo
#se crea clase Tienda
class Tienda():
    def __init__(self):
        #en registro de guardaran los dispositivos
        self.regitro = []
        
    #agrega dispositivo
    def agregar_dispositivo(self,dispositivo):
        print(f"{dispositivo.descripcion()}, y su precio es de: ${dispositivo.get_precio()}")
        self.regitro.append(dispositivo)
        
    #muestra catalogo
    def mostrar_catalogo(self):
        print("PRODUCTOS DISPONIBLES")
        total = 0
        for dispositivo in self.regitro:
            print(f"{dispositivo.descripcion()}, y su precio es de: ${dispositivo.get_precio()}")
            
            total = dispositivo.get_precio()
            
        print(f"valor del inventario {total}")
            