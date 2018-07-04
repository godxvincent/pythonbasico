from tkinter import *

# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Titulo de la Ventana")
# Controla el redimensionamiento el primero es el alto y el segundo el ancho
# son como booleanos 1 = true, 0 = false
# root.resizable(0, 0)
# Asignar iconos, para ubuntu los iconos deben ser icono.xbm
root.iconbitmap("hola.ico")
root.config(cursor="arrow", bg="blue", bd=15, relief="ridge")

# Se puede establecer un ancho y una altura al frame.
frame = Frame(root, width=480, heigh=320)
# Otras propiedas que pueden aplicarse cuando se hace el pack es decirle hacia
# que lado empaquetar el componente se puede usar el atributo side con valores
# como bottom, top, left, right y el anchor es el segundo atributo para
# indicar hacie que lado usando valores como n(north), s(south), e(east),
# w(west)
# frame.pack(side="bottom", anchor="e")
# Rellenar el frame al tamaño del contenedor. con X cubre horizontalmente,
# para expandir en vertical toca con y y usar el expand con el valor 1.
frame.pack(fill="both", expand=1)
frame.config(cursor="pirate", bg="lightblue", bd=25, relief="sunken")


root.mainloop()
