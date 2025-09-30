"""
    Objetivo: Probar metodo grid
    Fecha: 30-09-2025
"""
import tkinter as tk
from tkinter import messagebox

def realizar_saludo():
    dato = nombre.get()
    dato_largo = texto_largo.get('1.0', tk.END) # indicar posicion de inicio y posicion final del texto
    messagebox.showinfo(f"{dato}", f'{dato_largo}')
    
root = tk.Tk()
#  Definir prpiedades de la ventana principal
root.title("Mi primera ventana")
root.geometry("300x200") # ancho x alto

etiqueta = tk.Label(root, text="Bienvenido a Tkinter", font="Arial, 14")
etiqueta.grid(row=0, column=0)

nombre = tk.Entry(root)
nombre.grid(row=1,column=0)

boton = tk.Button(root, text='Saludo', command=realizar_saludo)
boton.grid(row=2, column=0)

boton2 = tk.Button(root, text='Salir', command=root.quit)
boton2.grid(row=2, column=1)

texto_largo = tk.Text(root, height=4, width=30)
texto_largo.grid(row=3, column=0)
root.mainloop()