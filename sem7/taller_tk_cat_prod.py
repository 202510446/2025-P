"""""
    objetivo: Var Tkinder con diccionario. triplas y arreglas
    fecha: 09-10-2025
"""""

import tkinder as tk
from tkinder import tkk, messengbox



class Almacen:
    
    categorias = ("Tecnologia", "hogar","ropa","alimentos") # tupla
    productos = [] # lista
# --- Funciones de control ---
    def agregar_producto(self):
        codigo = self.txt_codigo.get()
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
        productos.append(producto)
        self.actualizar_treevie
        self.limpiar_campos()

    def modiicar_producto(self):
        pass
    def eliminar_producto(self):
        pass
    def limiar_campos(self):
        pass
    def seleccionar_registro():
        pass
 
 
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestion de Productos con tkinter")
        self.ventana.geometry("700x400")
        self.ventana.config(padx=10, pady=10)
        
        #frame del formulario
        frm_form = Frame(ventana)
        frm_form.pack(fill=X, pady=10)
        Label(frm_form, text="Código:").grid(row=0, column=0, padx=5, pady=5,
        sticky=E)
        txt_codigo = Entry(frm_form)
        txt_codigo.grid(row=0, column=1, padx=5, pady=5)
        Label(frm_form, text="Nombre:").grid(row=1, column=0, padx=5, pady=5,
        sticky=E)
        txt_nombre = Entry(frm_form)
        txt_nombre.grid(row=1, column=1, padx=5, pady=5)


        Label(frm_form, text="Categoría:").grid(row=0, column=2, padx=5, pady=5,
        sticky=E)
        cbo_categoria = ttk.Combobox(frm_form, values=categorias, state="readonly")
        cbo_categoria.grid(row=0, column=3, padx=5, pady=5)
        Label(frm_form, text="Precio:").grid(row=1, column=2, padx=5, pady=5,
        sticky=E)
        txt_precio = Entry(frm_form)
        txt_precio.grid(row=1, column=3, padx=5, pady=5)


        
        Label(frm_form, text="Categoría:").grid(row=0, column=2, padx=5, pady=5,sticky=E)
        cbo_categoria = ttk.Combobox(frm_form, values=self.categorias, state="readonly")
        cbo_categoria.grid(row=0, column=3, padx=5, pady=5)
        Label(frm_form, text="Precio:").grid(row=1, column=2, padx=5, pady=5,sticky=E)
        txt_precio = Entry(frm_form)
        txt_precio.grid(row=1, column=3, padx=5, pady=5) 
        
        # --- Botones ---
        self.frm_btn = tk.Frame(self.ventana)
        self.frm_btn.pack(pady=10)
        
        tk.Button(self.frm_btn, text="Agregar", width=10,command=self.agregar_producto).grid(row=0, column=0, padx=5)
        tk.Button(self.frm_btn, text="Modificar", width=10,command=self.modificar_producto).grid(row=0, column=1, padx=5)
        tk.Button(self.frm_btn, text="Eliminar", width=10,command=self.eliminar_producto).grid(row=0, column=2, padx=5)
        tk.Button(self.frm_btn, text="Limpiar", width=10,command=self.limpiar_campos).grid(row=0, column=3, padx=5)
        
        # --- TreeView ---
        self.frm_tree = tk.Frame(self.ventana)
        self.frm_tree.pack(fill=tk, expand=True)
        columnas = ("Código", "Nombre", "Categoría", "Precio")
        self.tree = tk.Treeview(self.frm_tree, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
            self.tree.pack(fill=tk, expand=True)
            self.tree.bind("<ButtonRelease-1>", self.seleccionar_registro)

        self.ventana.mainloop()

            
            
if __name__ == '__main__':
    app = Almacen()
#    app.ventana.mainloop()