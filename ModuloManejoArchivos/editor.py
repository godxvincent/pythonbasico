from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = ""  # Se usa para almacenar la ruta del fichero a trabajar.


def nuevo():
    global ruta
    monitorStringVar.set("Creando archivo")
    ruta = ""
    # Borra desde el caracter 1 hasta el final.
    texto.delete(1.0, "end")


def abrir():
    global ruta
    monitorStringVar.set("Abriendo archivo")
    ruta = FileDialog.askopenfilename(initialdir=".",
                                      filetype=(("Ficheros de texto", "*.txt"),),
                                      title="Abrir archivo de texto")
    if ruta != "":
        fichero = open(ruta, "r")
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi Editor")


def guardar():
    # global ruta
    monitorStringVar.set("Guardando archivo")
    if ruta != "":
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        monitorStringVar.set("Archivo guardado correctamente")
    else:
        guardar_como()


def guardar_como():
    global ruta
    monitorStringVar.set("Guardando archivo como")
    fichero = FileDialog.asksaveasfile(title="Guardar como", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        monitorStringVar.set("Archivo guardado correctamente")
    else:
        monitorStringVar.set("Guardado cancelado")
        ruta = ""


# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Mi editor")
# root.iconbitmap("hola.ico")

# Un menu no se empaqueta se adiciona en la parte superior del root.
menubar = Menu(root)
root.config(menu=menubar)

# el tearoff es para quitar esa opción por default que carga un menu.
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
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

# Caja de texto
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("consolas", 12))


# Monitor inferior
monitorStringVar = StringVar()
monitorStringVar.set("Bienvenido a tu editor")
monitor = Label(root, textvar=monitorStringVar, justify="left")
monitor.pack(side="left")

root.mainloop()
