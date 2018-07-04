import sqlite3

conexion = sqlite3.connect("basedatos.db")

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE usuario (nombre VARCHAR(100),  edad INTEGER, email VARCHAR(100))")

# cursor.execute("INSERT INTO usuario values ('Ricardo',31,'godxvincent@gmail.com')")

# cursor.execute("SELECT * FROM usuario")
# usuario = cursor.fetchone()
# print(usuario)

# usuarios = [
#     ('Mario', 14, 'Mario@gmail.com'),
#     ('Julio', 24, 'Julio@gmail.com'),
#     ('Carmen', 34, 'Carmen@gmail.com')
# ]
#
# cursor.executemany("INSERT INTO usuario VALUES (?,?,?)", usuarios)

# cursor.execute("SELECT * FROM usuario")
# usuarios = cursor.fetchall()
# for usuario in usuarios:
#     print(usuario)

usuarios = [
    ('Daniela', 44),
    ('Carmenza', 54),
    ('Carlos', 64)
]
# El número de interrogantes corresponde al número de campos que se
# proporcionará en las tuplas
cursor.executemany("INSERT INTO usuario (nombre, edad) VALUES (?,?)", usuarios)

conexion.commit()
conexion.close()
