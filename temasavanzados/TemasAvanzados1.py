# Agrupar operaciones lógicas.
def funcionOperadoresEncadenados():
    numero = 35
    if numero >= 0 and numero <= 100:
        print("El número {} es mayor que cero y menor que 100".format(numero))
    else:
        print("El número {} NO es mayor que cero y menor que 100".format(numero))

    if 0 <= numero <= 100:
        print("El número {} es mayor que cero y menor que 100".format(numero))
    else:
        print("El número {} NO es mayor que cero y menor que 100".format(numero))


# Comprension de listas
# Metodo tradicional
def funcionComprensionListas():
    lista = []
    for letra in "casa":
        lista.append(letra)
    print(lista)

    lista = []
    for numero in range(1, 11):
        lista.append(numero**2)
    print(lista)

    lista = []
    for numero in range(1, 11):
        if numero % 2 == 0:
            lista.append(numero)
    print(lista)

    lista = []
    for numero in range(1, 11):
        lista.append(numero**2)

    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    print(pares)

    # Metodo de comprensión
    lista2 = [letra for letra in "casa"]
    print(lista2)

    lista2 = [numero**2 for numero in range(1, 11)]
    print(lista2)

    lista2 = [numero for numero in range(1, 11) if numero % 2 == 0]
    print(lista2)

    pares = [par for par in [numero**2 for numero in range(1, 11)] if par % 2 == 0]
    print(pares)

# Funciones decoradoras parte I


def Hola():
    def Saludo():
        return "Hola Mundo"
    return Saludo


def funcionesDecoradorasParteI():
    print(Hola())
    funcionSaludo = Hola()
    print(funcionSaludo())
    print("Funcion globals")
    print(globals())
    print("Funcion locals")
    print(locals())


def Hola_2():
    print("Hola!")


def Adios_2():
    print("Adios!")


def monitorizar(funcion):

    def decorar():
        print("Se va a ejecutar la funcion: ", funcion.__name__)
        funcion()
        print("Ha terminado la ejecución de la funcioón: ", funcion.__name__)
    return decorar


# Se puede ejecutar llamando de frente la funcion monitorizar.
monitorizar(Hola_2)()


# Pero al decorar la funcion con el nombre de la función que la va a
# decorar se llama directamente la funcion a usar
@monitorizar
def Hola_3():
    print("Hola!")


@monitorizar
def Adios_3():
    print("Adios!")


print("Ejecución de las funciones de forma directa")

Hola_3()

# Para el manejo de parametros se debe adicionar a la funcion decoradora
# los argumentos de forma dinamica

print("***** Decoradores con argumentos ******")


def monitorizar_2(funcion):

    def decorar(*args, **kwargs):
        print("Se va a ejecutar la funcion: ", funcion.__name__)
        funcion(*args, **kwargs)
        print("Ha terminado la ejecución de la funcioón: ", funcion.__name__)
    return decorar


@monitorizar_2
def Hola_4(nombre):
    print("Hola {}!".format(nombre))


Hola_4("Ricardo")
