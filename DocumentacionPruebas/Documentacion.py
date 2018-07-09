"""Este es el docstring de mi modulo de documentación"""
# Docstring


def Hola(args):
    """Este es un ejemplo del Docstring"""
    print("Hola ", args, "!")


Hola("Ricardo")

print(help(Hola))


class Clase:
    """Este es el docstring de la clase"""

    def __init__(self):
        """Este es el docstring del constructor"""
        pass

    def metodo(self):
        """Este es el docstring del metodo"""
        pass


print(help(Clase))

# para ver la documentacion desde la consola se debe ejecutar el comando pydoc
# con pydoc -w mimodulo  se creara un archivo html con la documentación creada
# con pydoc -w mipquete ./ para que genere toda la documentación del paquete
# con pydoc - b sube un servidor local simulando toda la documentación
# pydoc -p puertoasubir -b
Modulo epidoc y sphinx para mejor documentacion
