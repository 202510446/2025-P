"""
    objetivo: gestionar archivos, solo para lectura del contenido
    Fecha: 28-10-2025
"""
class Archivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.arreglo = []

    def abrir(self):
         with open(self.nombre_archivo, 'r', encoding='UTF-8') as archivo:
                for linea in archivo:
                    partes = linea.strip().split(',') 
                    self.arreglo.append(partes)
    
    def cerrar(self):
        pass

    def mostrar(self):
        return self.arreglo
if __name__ == "__main__":
    oArch=Archivo("producto.txt")
    oArch.abrir()
    print(oArch.mostrar())
