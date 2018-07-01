from tkinter import *

# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Titulo de la Ventana")
root.iconbitmap("hola.ico")

# Se puede establecer un ancho y una altura al frame.
frame = Frame(root, width=480, heigh=320)
frame.pack()

label = Label(frame, text="Etiqueta")
# Al usar pack() ignora el tamaño dado al frame y reajusta todo al contenido
# del label.
label.place(x=10, y=10)

root.mainloop()
