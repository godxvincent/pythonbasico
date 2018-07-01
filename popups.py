from tkinter import *
from tkinter import messagebox as MessageBox


def test():
    # MessageBox.showinfo("Titulo Ventana", "Mensaje Ventana")
    # MessageBox.showwarning("Alert", "Sección solo administradores")
    # MessageBox.showerror("Error", "Ha ocurrido un error inesperado")
    # resultado = MessageBox.askquestion("Salir", "Esta seguro que desea salir sin guardar?")
    # if resultado == "yes":  # "no"
    #     root.destroy()
    # resultado = MessageBox.askokcancel("Salir", "Esta seguro que desea salir sin guardar?")
    # if resultado:  # true o false
    #     root.destroy()
    # resultado = MessageBox.askyesnocancel("Salir", "Esta seguro que desea salir sin guardar?")
    # if resultado:  # true o false
    #     root.destroy()
    resultado = MessageBox.askretrycancel("Reintentar", "No hubo conexión")
    if resultado:  # true o false
        root.destroy()


# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Titulo de la Ventana")
root.iconbitmap("hola.ico")


Button(text="Haz click", command=test).pack()

root.mainloop()
