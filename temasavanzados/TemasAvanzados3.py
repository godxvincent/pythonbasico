# Expresiones regulares
import re


def basico():
    texto = "En esta cadena se encuentra una palabra mágica"

    resultado = re.search("mágica", texto)
    print(resultado)
    resultado = re.search("hola", texto)
    print(resultado)

    resultado = re.search("mágica", texto)
    print(resultado)
    print(resultado.start())
    print(resultado.end())
    print(resultado.span())

    # Match busca el texto solo en el inicio de la cadena de texto.
    resultado = re.match("Hola", texto)
    print(resultado)

    lista = re.split(' ', texto)
    print(lista)

    print(re.sub("palabra", "mundo", texto))

    print(re.findall("ra|ca", texto))


def buscar(patrones, texto):
    for patron in patrones:
        print("| {} | \t\t {}".
              format(patron, re.findall(patron, texto)))


# El asterisco(*) busca ninguna o varias repeticiones de la letra a la izquierda
# del asterisco
# El más(+) busca una o varias repeticiones de la letra a la izquierda
# del caracter
# La interrogante(?) busca una o ninguna repeticioón de la letra a la izquierda
# del caracter
print("Ejemplos con asterisco, más e interrogación")
texto = "hla hola hoola hooola hoooooola"
patrones = ['ho', 'ho*', 'ho*la', 'hu*la', 'ho+la', 'ho?', 'ho?la']
buscar(patrones, texto)


# la sentencia {n} indica cuantos caracteres a la izquierda se espera encontrar
print("Ejemplos con rango de caracteres")
patrones = ["ho{0}la", "ho{1}", "ho{0,2}la", "ho{2,10}la"]
buscar(patrones, texto)

print("Ejemplos con conjuntos")
texto = "hala hela hila hola hula"
patrones = ['h[ou]la', 'h[aio]la', 'h[aeiou]la']
buscar(patrones, texto)

# Con las llaves cuadradas se definen conjuntos de caracteres que se desean
# buscar
print("Ejemplos con conjunto de caracteres")
texto = "hala hela hila hola hula"
patrones = ['h[ou]la', 'h[aio]la', 'h[aeiou]la', 'h[^o]la']
buscar(patrones, texto)

print("Ejemplos con conjunto de caracters y rango de numero de caracteres")
texto = "haala heeela hiiiiiila hooooooola haela"
patrones = ['h[ae]la', 'h[ae]*la', 'h[io]{3,9}la']
buscar(patrones, texto)


# [a-z]
# [A-Z]
# [A-Za-z]
# [A-z]
# [0-9]
# [a-zA-Z0-9]

print("Ejemplos con rangos de caracteres en el conjunto")
texto = "hola h0la Hola mola m0la M0la sdjh asdr U377 Ysdj"
patrones = ['h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}']
buscar(patrones, texto)

# \d numéricos
# \D No numericos
# \s espacio en blanco
# \S no espacio en blanco
# \w alfanumerico
# \W no alfanumerico

print("Ejemplos con caracteres escapados, en python se debe anteponer una r para usarlos")
texto = "Este curso de Python 3 se publicó en 2018"
patrones = [r'\d', r'\d+', r'\D', r'\D+', r'\s', r'\S', r'\w', r'\w+', r'\W', r'\W+']
buscar(patrones, texto)
