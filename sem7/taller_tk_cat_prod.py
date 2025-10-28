"""
    Objetivo: Uar Tkinter con diccionarios, tuplas y arreglos
    Fecha: 09-10-2025    
"""
import tkinter as tk
from tkinter import ttk, messagebox



class Almacen:
    
    categorias = ("Tecnología", "Hogar", "Ropa", "Alimentos") # tupla
    productos = [] # lista

# --- Funciones de control ---
    def agregar_producto(self):
        codigo = self.txt_codigo.get()
        nombre = self.txt_nombre.get()
        categoria = self.cbo_categoria.get()
        precio = self.txt_precio.get()

        if not codigo or not nombre or not categoria or not precio:
            messagebox.showwarning("Validación", "Todos los campos son obligatorios")
            return

        # Diccionario del producto
        producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": float(precio)
        }
        self.productos.append(producto)
        self.actualizar_treeview()
        self.limpiar_campos()

    def actualizar_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for prod in self.productos:
            self.tree.insert("", "end", values=(prod["codigo"], prod["nombre"], prod["categoria"], prod["precio"]))
    
    def modificar_producto(self):
        pass
    def eliminar_producto(self):
        pass
    def limpiar_campos(self):
        self.txt_codigo.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.cbo_categoria.set("")
        self.txt_precio.delete(0, tk.END)
        
    def seleccionar_registro(self, event):
            seleccionado = self.tree.focus()
            if not seleccionado:
                return

            valores = self.tree.item(seleccionado, "values")
            self.txt_codigo.delete(0, tk.END)
            self.txt_codigo.insert(0, valores[0])
            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(0, valores[1])
            self.cbo_categoria.set(valores[2])
            self.txt_precio.delete(0, tk.END)
            self.txt_precio.insert(0, valores[3])
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Productos con Tkinter")
        self.ventana.geometry("700x400")
        self.ventana.config(padx=10, pady=10)
        
        # frame del formulario
        self.frm_form = tk.Frame(self.ventana)
        self.frm_form.pack(fill=tk.X, pady=10)
        
        tk.Label(self.frm_form, text="Código:").grid(row=0, column=0, padx=5, pady=5,sticky=tk.E)
        self.txt_codigo = tk.Entry(self.frm_form)
        self.txt_codigo.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.frm_form, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.txt_nombre = tk.Entry(self.frm_form)
        self.txt_nombre.grid(row=1, column=1, padx=5, pady=5)
         
        tk.Label(self.frm_form, text="Categoría:").grid(row=0, column=2, padx=5, pady=5,sticky=tk.E)
        self.cbo_categoria = ttk.Combobox(self.frm_form, values=self.categorias, state="readonly")
        self.cbo_categoria.grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(self.frm_form, text="Precio:").grid(row=1, column=2, padx=5, pady=5,sticky=tk.E)
        self.txt_precio = tk.Entry(self.frm_form)
        self.txt_precio.grid(row=1, column=3, padx=5, pady=5)

        # --- Botones ---
        self.frm_btn = tk.Frame(self.ventana)
        self.frm_btn.pack(pady=10)
        
        tk.Button(self.frm_btn, text="Agregar", width=10,command=self.agregar_producto).grid(row=0, column=0, padx=5)
        tk.Button(self.frm_btn, text="Modificar", width=10,command=self.modificar_producto).grid(row=0, column=1, padx=5)
        tk.Button(self.frm_btn, text="Eliminar", width=10,command=self.eliminar_producto).grid(row=0, column=2, padx=5)
        tk.Button(self.frm_btn, text="Limpiar", width=10,command=self.limpiar_campos).grid(row=0, column=3, padx=5)

        # --- TreeView ---
        self.frm_tree = tk.Frame(self.ventana)
        self.frm_tree.pack(fill=tk.BOTH, expand=True)
        columnas = ("Código", "Nombre", "Categoría", "Precio")
        self.tree = ttk.Treeview(self.frm_tree, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
            self.tree.pack(fill=tk.BOTH, expand=True)
            self.tree.bind("<ButtonRelease-1>", self.seleccionar_registro)
            
        self.ventana.mainloop()

if __name__ == '__main__':
    app = Almacen()
#    app.ventana.mainloop()