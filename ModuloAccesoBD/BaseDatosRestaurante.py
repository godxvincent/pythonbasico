import sqlite3
import os


def crear_db():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        sentencia = """CREATE TABLE categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL) """
        cursor.execute(sentencia)
    except sqlite3.OperationalError:
        print("La tabla categoria ya fue creada")
    except Exception as e:
        print(type(e).__name__)
    finally:
        print("Continua con el proceso")

    try:
        sentencia = """CREATE TABLE plato(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) UNIQUE NOT NULL,
        categoria_id INTEGER NOT NULL,
        FOREIGN KEY(categoria_id) REFERENCES categoria(id))"""
        cursor.execute(sentencia)
    except sqlite3.OperationalError:
        print("La tabla plato ya fue creada")
    except Exception as e:
        print(type(e).__name__)
    finally:
        print("Continua con el proceso")

    conexion.commit()
    conexion.close()


def agregar_categoria():
    os.system("cls")
    while (True):

        print("Por favor ingresar una categoria")
        categoria = input()
        listaCategorias = []
        listaCategorias.append(categoria.title())
        try:
            conexion = sqlite3.connect("restaurante.db")
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO categoria VALUES (null,?)",
                           listaCategorias)
        except sqlite3.IntegrityError:
            print("**********************ERROR*************************")
            print("La categoria {} ya esta registrada".format(categoria))
            print("**********************ERROR*************************")
        except Exception as e:
            print(type(e).__name__)
        else:
            print("Categoria creada exitosamente")
            break
        finally:
            conexion.commit()
            conexion.close()


def agregar_plato():
    # Se cargan las categorias disponibles.
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM categoria")
    categorias = cursor.fetchall()

    conexion.commit()
    conexion.close()

    os.system("cls")
    while (True):
        print("Por favor ingrese el nombre del plato que desea registrar")
        nombrePlato = input()
        print("Por favor indique a cual categoria pertenece el plato")
        for categoria in categorias:
            print("Código Categoria '{}', Nombre Categoria '{}'".
                  format(categoria[0], categoria[1]))
        idCategoria = input()
        try:
            platoTupla = (nombrePlato.title(), int(idCategoria))
            conexion = sqlite3.connect("restaurante.db")
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO plato VALUES (null,?,?)", platoTupla)
        except sqlite3.IntegrityError:
            print("El plato {} ya se encuentra registrado".
                  format(nombrePlato, idCategoria))
        except Exception as e:
            print(type(e).__name__)
            break
        else:
            print("Plato registrado correctamente")
            break
        finally:
            conexion.commit()
            conexion.close()


def visualizar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT a.nombre, b.nombre FROM categoria a join plato b on (a.id = b.categoria_id)")
    menu = cursor.fetchall()
    for plato in menu:
        print("Categoria: {} - Plato: {}".format(plato[0], plato[1]))
    conexion.commit()
    conexion.close()


def menuOpciones():
    os.system("cls")
    while True:
        print("********************************************************")
        print("Bienvenido al menu para adicionar categorias de platos ")
        print("Ingrese opción 1 para adicionar nuevas categorias")
        print("Ingrese opción 2 para adicionar un plato a una categoria")
        print("Ingrese opción 3 para visualizar el menú")
        print("Ingrese opción 4 para salir del menú")
        print("*******************************************************")
        opcion = input("Ingrese una opción\n")
        if opcion == "1":
            agregar_categoria()
        elif opcion == "2":
            agregar_plato()
        elif opcion == "3":
            visualizar_menu()
        elif opcion == "4":
            print("Gracias por usar nuestro sistema")
            break
        else:
            print("***Opción no válida***")


# crear_db()
menuOpciones()
