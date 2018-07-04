from tkinter import *


def seleccionar():
    cadena = ""
    if leche.get() == 1:
        cadena += "Con leche"
    else:
        cadena += "Sin leche"

    if azucar.get() == 1:
        cadena += " y con azúcar"
    else:
        cadena += " y sin azúcar"
    monitor.config(text=cadena)


# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Cafetería")
root.config(bd=15)
root.iconbitmap("hola.ico")

leche = IntVar()  # 1 = si, 0 = no
azucar = IntVar()  # 1 = si, 0 = no

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")
Label(frame, text="¿Como quieres el café?").pack(anchor="w")
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0,
            command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0,
            command=seleccionar).pack(anchor="w")

monitor = Label(frame, text="")
monitor.pack()

root.mainloop()
