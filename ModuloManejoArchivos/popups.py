from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog


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
    # resultado = MessageBox.askretrycancel("Reintentar", "No hubo conexión")
    # if resultado:  # true o false
    #     root.destroy()
    # color = ColorChooser.askcolor(title="Elige un color!")
    # print(color)
    # askopenfilename Devuele una ruta
    # ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:",
    #                                   filetypes=(("Archivos de texto", "*.txt"),
    #                                              ("Archivos PDF", "*.pdf"),
    #                                              ("Todos los archivos", "*.*")))
    # print(ruta)
    # asksaveasfile Devuele un fichero
    fichero = FileDialog.asksaveasfile(
        title="Guardar un fichero", defaultextension=".txt", mode="w")
    if fichero is not None:
        fichero.write("Esto es un texto de prueba")
        fichero.close()


# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Titulo de la Ventana")
root.iconbitmap("hola.ico")


Button(text="Haz click", command=test).pack()

root.mainloop()
