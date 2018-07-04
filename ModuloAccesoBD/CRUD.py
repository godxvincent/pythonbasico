import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM USUARIO WHERE ID = 1")

usuarios = cursor.fetchone()
print(usuarios)

conexion.commit()
conexion.close()
