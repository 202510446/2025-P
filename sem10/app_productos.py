"""
    objetivo: gestionar los datos del archivo producto.txt através de la aplicacion de tkinter
    Fecha: 28-10-2025
"""
import tkinter as tk
from gestor_archivos import Archivo
from tkinter import ttk,messagebox

class Ventana:
    def buscar(self,codigo):
        codigo=int(self.ent_codigo.get())
        for linea in self.arreglo_datos:
                if codigo == int(linea[0]):
                    self.txt_descripcion.set(linea[1])
                    self.txt_precio.set(linea[2])
                    return
        messagebox.showinfo("alerta","Codigo no encontrado")
        self.txt_descripcion.set("")
        self.txt_precio.set("")
        
    def menor(self):
        menor=999
        for linea in self.arreglo_datos:
            if float(linea[2]) < menor:
                menor = float(linea[2])
        messagebox.showinfo("precio menor",f"El precio menor es: {menor}")
    
    def sumar(self):
        suma =0
        for linea in self.arreglo_datos:
            suma += float(linea[2])
        messagebox.showinfo("mensaje",f"La suma de los precios es: {suma}")
        
    def cargar_datos(self):
        for fila in self.arreglo_datos:
            self.tree.insert("",tk.END, values=fila)
            
            
    def __init__(self, principal):
        self.principal = principal
        self.principal.title("Gestor de archivos de productos")
        self.principal.geometry("600x400")
        self.archivo = Archivo('producto.txt')
        self.archivo.abrir()
        self.arreglo_datos= self.archivo.arreglo
        
        #texto variable
        self.txt_descripcion = tk.StringVar()
        self.txt_descripcion.set("")
        self.txt_precio = tk.StringVar()
        self.txt_precio.set("")

        #etiquetas-
        self.frm_etiquetas = tk.Frame(principal)
        self.frm_etiquetas.pack()

        tk.Label(self.frm_etiquetas, text='Codigo ').grid(row=0, column=0,padx=5, pady=5, sticky='w')
        tk.Label(self.frm_etiquetas, text='Descripcion ').grid(row=1, column=0,padx=5, pady=5, sticky='w')
        tk.Label(self.frm_etiquetas, text='Precio ').grid(row=2, column=0,padx=5, pady=5, sticky='w')

        self.lbl_descripcion = tk.Label(self.frm_etiquetas, textvariable=self.txt_descripcion).grid(row=1, column=1,padx=5, pady=5, sticky='w')
        self.lbl_precio = tk.Label(self.frm_etiquetas, textvariable=self.txt_precio).grid(row=2, column=1,padx=5, pady=5, sticky='w')

        # entries-espacios para ingresar datos
        self.ent_codigo = tk.Entry(self.frm_etiquetas)
        self.ent_codigo.grid(row=0, column=1, padx=5, pady=5, sticky='w')


        
        #botones
        self.frm_botones = tk.Frame(principal)
        self.frm_botones.pack()
        self.btn_buscar = tk.Button(self.frm_botones, text='buscar', command=self.buscar)
        self.btn_buscar.grid(row=0, column=0,padx=10)

        self.btn_menor = tk.Button(self.frm_botones, text='precio menor', command=self.menor)
        self.btn_menor.grid(row=0, column=1,padx=10)

        self.btn_sumar = tk.Button(self.frm_botones, text='sumar', command=self.sumar)
        self.btn_sumar.grid(row=0, column=2,padx=10)

        #treeview
        self.tree = ttk.Treeview(self.principal, columns=('codigo','descripcion','precio'), show='headings')
        for col in self.tree['columns']:
            self.tree.heading(col, text=col.capitalize())
            self.tree.pack(expand=True, fill='both', pady=10)
            
        #poblar el treeview con el contenido del arreglo
        self.cargar_datos()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana(root)
    root.mainloop()