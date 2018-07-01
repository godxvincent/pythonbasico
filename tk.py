from tkinter import *

root = Tk()

root.title("Titulo de la Ventana")

# Controla el redimensionamiento el primero es el alto y el segundo el ancho
# son como booleanos 1 = true, 0 = false
root.resizable(0, 0)

# Asignar iconos, para ubuntu los iconos deben ser icono.xbm
root.iconbitmap("hola.ico")

root.mainloop()
