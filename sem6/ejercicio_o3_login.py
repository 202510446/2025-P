"""
    Objetivo: Uso combinado de los metodos pack y grid
    Fecha: 30-09-2025
"""
import tkinter as tk
from tkinter import messagebox

contador = 0

def aceptar():
    global contador
    if ent_user.get() == 'urp' and ent_pass.get() == 'IF201':
        messagebox.showinfo('Login', 'Bienvenido al Sistema')
        contador = 0
    else:
        contador +=1
        if contador > 3:
            messagebox.showerror('Login', 'Ud. no esta autorizado a usar el sistema')
            root.destroy()
        else:
            messagebox.showerror('Login', 'Usuario o contraseña incorrecto')

root = tk.Tk()
#  Definir prpiedades de la ventana principal
root.title("Identificación de Usuario")
root.geometry("300x250") # ancho x alto
root.configure(background="lightgray")

login = tk.Label(root, text='Login', font='Arial, 14', background="lightgray")
login.pack()

# Nuevo frame para user y pass
frame_user = tk.Frame(root, background="lightgray")
etiq_user = tk.Label(frame_user, text='Usuario:', background="lightgray")
etiq_user.grid(row=0, column=0)
ent_user = tk.Entry(frame_user)
ent_user.grid(row=0, column=1)
etiq_pass = tk.Label(frame_user, text='Contraseña:', background="lightgray")
etiq_pass.grid(row=1, column=0)
ent_pass = tk.Entry(frame_user, show='*')
ent_pass.grid(row=1, column=1)
frame_user.pack()

# Nuevo frame para los botones
frame_butt = tk.Frame(root, background="lightgray")
btn_aceptar = tk.Button(frame_butt, text='Aceptar', command=aceptar, background='Light Blue')
btn_aceptar.grid(row=0, column=0, padx=10, pady=10)
btn_salir = tk.Button(frame_butt, text='Salir', command=root.quit, width=7, background='Light Blue')
btn_salir.grid(row=0, column=1, padx=10, pady=10)
frame_butt.pack()

# agrega una imagen
img = tk.PhotoImage(file='logo_urp.png')
etiq = tk.Label(root, image=img)
etiq.pack()

root.mainloop()