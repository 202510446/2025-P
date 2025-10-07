
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
etiqueta.pack()

nombre = tk.Entry(root)
nombre.pack()

boton = tk.Button(root, text='Saludo', command=realizar_saludo)
boton.pack()

texto_largo = tk.Text(root, height=4, width=30)
texto_largo.pack()

root.mainloop() # Inicia el loop de la interfaz