from tkinter import *

# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Titulo de la Ventana")
root.iconbitmap("hola.ico")

# Un menu no se empaqueta se adiciona en la parte superior del root.
menubar = Menu(root)
root.config(menu=menubar)

# el tearoff es para quitar esa opción por default que carga un menu.
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="nuevo")
filemenu.add_command(label="abrir")
filemenu.add_command(label="guardar")
filemenu.add_command(label="cerrar")
filemenu.add_separator()
filemenu.add_command(label="salir", command=root.quit)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="cortar")
editmenu.add_command(label="copiar")
editmenu.add_command(label="pegar")
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

# Adiciona los sub menus a la barra de menu.
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)


root.mainloop()
