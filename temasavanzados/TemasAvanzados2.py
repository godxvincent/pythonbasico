# # Funciones generadoras e iteradores
# # Una funcion generadora retorna una información iterable
# # en lugar de usar return se debe usar yield.
#
#
# def pares(numeroFinal):
#     for numero in range(numeroFinal+1):
#         if numero % 2 == 0:
#             yield numero
#
#
# print(pares(10))
# for n in pares(10):
#     print(n)
#
# lista = [numero for numero in pares(20)]
# for n in lista:
#     print(n)
#
# # Las listas y las cadenas no se puede operar, para hacer esto se deben
# # convertir a objetos iterables con la funcion iter
# print("Imprimiendo un elemento de la lista_iterable")
# lista_iterable = iter(lista)
# print(next(lista_iterable))
#
# cadena_iterable = iter("Hola Mundo")
# print(next(cadena_iterable))
#
# # funciones lambda
# # Son formas reducidas de una función, deben ser una expresión minimaself.
# print("Funciones lambda")
#
#
# def doblarNumero(numero):
#     return numero * 2
#
#
# # doblarNumeroLambda = lambda numero: numero * 2
# # El editor me actualiza el código y lo deja como una función normal.
# def doblarNumeroLambda(numero): return numero * 2
#
#
# print(doblarNumero(54))
# print(doblarNumeroLambda(54))

# Funcion Filter
print("Función Filter")

listaNumeros = range(1, 101)


def multiplos(numero):
    if numero % 5 == 0:
        return True


listaF = list(filter(multiplos, listaNumeros))
print(listaF)

print("con funciones lambda (filter y map)")

listaF2 = list(filter(lambda numero: numero % 5 == 0, listaNumeros))
print(listaF2)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Soy {} y tengo {} años".format(self.nombre, self.edad)


personas = [
    Persona("Juan", 15),
    Persona("Carlos", 35),
    Persona("Maria", 14),
    Persona("Diana", 78)
]

menores = list(filter(lambda persona: persona.edad < 18, personas))
for menor in menores:
    print(menor)

lista = range(1, 20)

# La función MAP recibe una función y le aplica la operacion al objeto
listaF = list(map(lambda numero: numero * 2, lista))
print(listaF)

personasF = list(map(lambda persona: Persona(persona.nombre, persona.edad + 1),
                     personas))
for persona in personasF:
    print(persona)
