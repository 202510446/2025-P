""""
    objetivo: Empezar a trabajar con interfaz de presentacion de ventana
    fecha: 30-09-2025
"""

import tkinter as tk
from tkinter import messagebox

def ralizar_saludo():
    dato = nombre.get()
    dato_largo = texto_largo.get(1.0, tk.END)
    messagebox.showinfo(f"{dato}", f"{dato_largo}")
    
root = tk.Tk()
#definir propiedades de la ventana principal
root.title("Mi primera ventana ")
root.geometry("300x200") # ancho x altos

etiqueta = tk.Label(root, text="bienvenido a Tkinter",font="Arial 14")
etiqueta.pack() 

nombre= tk.Entry(root)
nombre.pack()

boton= tk.Button(root, text="Saludo",command=ralizar_saludo)
boton.pack()

texto_largo = tk.Text(root, height=4, width=30)
texto_largo.pack()

root.mainloop() # Inicia el loop de la ventana