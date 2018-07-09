# Se puede adicionar comandos dentro de la documentación que se ejecutaran.
# Entre los simbolos >>> se puede adicionar un comando para ejecutar la prueba
# Seguido se pone el resultado esperado de la prueba


def suma(a, b):
    """
    La funcion suma recibe dos parametros a y b
    Devuelve la suma de ambosself.

    >>> suma(5, 10)
    15

    >>> suma('aa','bb')
    'aabb'

    >>> l1 = [1, 2, 3]
    >>> l2 = [4, 5, 7]
    >>> suma(l1, l2)
    [1, 2, 3, 4, 5, 7]

    >>> suma(10, 'hola')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


def doblar(lista):
    """
    Función para duplicar el valor de unos elementos de una lista.
    >>> l = [1, 2, 3, 4, 5]
    >>> doblar(l)
    [2, 4, 6, 8, 10]

    >>> l = []
    >>> for i in range(10):
    ...     l.append(i)
    >>> doblar(l)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    return [ele * 2 for ele in lista]


# Para lanzar la prueba se debe adicionar el modulo doctest y llamar al metodo testmod()
# Para evitar que se lance el test cuando se importa el modulo desde otro fichero
# Se debe condicionar
if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Se ejecuta el script de forma normal, si no hay fallos no avisa si sale fallo
# sale un error similar a esto
# File "Tests.py", line 11, in __main__.suma
# Failed example:
#     suma(5, 15)
# Expected:
#     15
# Got:
#     20
# **********************************************************************
# 1 items had failures:
#    1 of   1 in __main__.suma
# ***Test Failed*** 1 failures.
# Para ver cuando no hay fallos entonces se llama el modulo con el parametro -v
# python Test.py -v
