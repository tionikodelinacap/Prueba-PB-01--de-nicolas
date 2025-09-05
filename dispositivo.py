# se crea la clase padre
class Dispositivo():
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio
    #getter para    
    def get_precio(self):
        return self.__precio
    
    # setter para modificar precio
    def set_precio(self,nuevo_precio):
        if self.__precio > 0:
            self.__precio = nuevo_precio
        else:
            print("elnumero debe ser mayor a 0")
        
    #descripcion de metodo
    def descripcion(self):
        return f"la marca del dispositivo es: {self.marca} y su precio es: {self.__precio}"
    