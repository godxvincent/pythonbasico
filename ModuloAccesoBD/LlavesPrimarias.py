import sqlite3

# Se crea la base de datos2 y luego  se crea la base de datos de productos.
# conexion = sqlite3.connect("basedatos2.db")
# conexion = sqlite3.connect("productos.db")
conexion = sqlite3.connect("usuarios_autoincremental2.db")

cursor = conexion.cursor()

# cursor.execute("""
#             CREATE TABLE usuario
#             (
#                 dni VARCHAR(9) PRIMARY KEY,
#                 nombre VARCHAR(100),
#                 edad INTEGER,
#                 email VARCHAR(100)
#             )
#             """)

# usuarios = [
#     (1, 'Mario', 14, 'Mario@gmail.com'),
#     (2, 'Julio', 24, 'Julio@gmail.com'),
#     (3, 'Carmen', 34, 'Carmen@gmail.com')
# ]
#
# cursor.executemany("INSERT INTO usuario VALUES (?,?,?,?)", usuarios)

# cursor.execute("""
#             CREATE TABLE producto
#             (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nombre VARCHAR(100) NOT NULL,
#                 marcar VARCHAR(50) NOT NULL,
#                 precio FLOAT NOT NULL
#             )
#             """)

# productos = [
#     ("teclado", "logitech", 19.45),
#     ("pantalla", "LG", 89.95)
# ]
#
# cursor.executemany("INSERT INTO PRODUCTO VALUES (null,?,?,?)", productos)

cursor.execute("""
            CREATE TABLE usuario
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dni VARCHAR(9) UNIQUE ,
                nombre VARCHAR(100),
                edad INTEGER,
                email VARCHAR(100)
            )
            """)

usuarios = [
    (1, 'Mario', 14, 'Mario@gmail.com'),
    (2, 'Julio', 24, 'Julio@gmail.com'),
    (3, 'Carmen', 34, 'Carmen@gmail.com')
]

cursor.executemany("INSERT INTO usuario VALUES (null,?,?,?,?)", usuarios)

conexion.commit()
conexion.close()
