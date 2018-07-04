from tkinter import *

# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Titulo de la Ventana")
root.iconbitmap("hola.ico")

texto = Text(root)
texto.pack()
# El ancho y alto corresponde a numero de caracteres y no pixeles.
texto.config(width=30, height=10, font=("consolas", 12), padx=15, pady=15,
             selectbackground="red")

root.mainloop()
