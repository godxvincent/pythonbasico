from tkinter import *


def hola():
    print("Hola Mundo")


# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Titulo de la Ventana")
root.iconbitmap("hola.ico")

boton = Button(root, text="Haz me click", command=hola)
boton.pack()
root.mainloop()
