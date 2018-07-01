from tkinter import *

# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Titulo de la Ventana")
root.iconbitmap("hola.ico")

texto = StringVar()
texto.set("Texto del StringVar")
# Se puede establecer un ancho y una altura al frame.
frame = Frame(root, width=480, heigh=320)
frame.pack()

label = Label(frame, text="Etiqueta")
# Al usar pack() ignora el tamaño dado al frame y reajusta todo al contenido
# del label.
label.place(x=10, y=10)
label.config(bg="green", fg="blue", font=("Verdana", 10))
# Se asigna al atributo textvariable la variable texto definida en linea 9.
label.config(textvariable=texto)
# Para adicionar una imagen se puede una jpg o gif con la clase PhotoImage
imagen = PhotoImage(file="imagen.gif")
imagen = imagen.subsample(2, 2)
# imagen = imagen.zoom(1,1) Para acercar la imagen.
label.config(image=imagen, bd=0)
# label.config(compound="right", width=140, heigh=20)
# Modulo externo para manejo de otros formatos de imagen.

root.mainloop()
