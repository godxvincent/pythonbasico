from tkinter import *


def seleccionar():
    monitor.config(text="{}".format(opcion.get()))


def reset():
    opcion.set(None)
    monitor.config(text="")


# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Titulo de la Ventana")
root.iconbitmap("hola.ico")

opcion = IntVar()

Radiobutton(root, text="Opción 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text="Opción 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text="Opción 3", variable=opcion, value=3, command=seleccionar).pack()
monitor = Label(root)
monitor.pack()
Button(root, text="reset", command=reset).pack()


root.mainloop()
