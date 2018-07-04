from tkinter import *

# Configurando la raiz de una aplicación de escritorio
root = Tk()
root.title("Titulo de la Ventana")
root.iconbitmap("hola.ico")

label = Label(root, text="Nombre:")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entrada = Entry(root)
entrada.grid(row=0, column=1, sticky="w", padx=5, pady=5)
entrada.config(justify="left", state="disable")  # el otro estado es "normal"

label2 = Label(root, text="Apellido:")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)
entrada2 = Entry(root)
entrada2.grid(row=1, column=1, sticky="w", padx=5, pady=5)
entrada2.config(justify="center", show="*")  # Show muestra el campo con el
# caracter indicado


root.mainloop()
