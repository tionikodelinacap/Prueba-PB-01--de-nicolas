#importa clases
from computadore import Computadora
from dispositivo import Dispositivo
from tablet import Tablet
from tienda import Tienda
from telefono import Telefono
# se crea una instancia
registro = Tienda()

# se crean los objetos con sus atributos(marca,modelo,precio y (camara,ram, tamaño de pantalla) )
telefono = Telefono("samsung","serie s",400000, 120)

tablet = Tablet("samsung","book",700000,11.6)

computador = Computadora("hp","xt",250000,24)

# se agregan los objetos a tienda
registro.agregar_dispositivo(telefono)     
registro.agregar_dispositivo(tablet)
registro.agregar_dispositivo(computador)

#muestra el catalogo de tienda
registro.mostrar_catalogo()




