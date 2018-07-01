from tkinter import *


def hola():
    print("Hola Mundo")


def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()


def restar():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()


def multiplicar():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()


def borrar():
    n1.set("")
    n2.set("")


# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Titulo de la Ventana")
root.iconbitmap("hola.ico")
root.config(padx=15, pady=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Numero 1").pack()
Entry(root, justify="center", textvariable=n1).pack()
Label(root, text="Numero 2").pack()
Entry(root, justify="center", textvariable=n2).pack()
Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()
Label(root, text=" ").pack()
Button(root, text="Sumar", command=sumar).pack(side=LEFT)
Button(root, text="Restar", command=restar).pack(side=LEFT)
Button(root, text="Multiplicar", command=multiplicar).pack(side=LEFT)

root.mainloop()
