class Vehiculo:
    velocidad = 0
    nombre = ""
class Terrestre(Vehiculo):
    def avanzar():
        'vehiculo terrestre avanzando--'
class Aereo(Vehiculo):
    altura_max = 0
    def __init__(self, altura):
        self.altura_max = altura
    def volar(self):
        return 'vehiculo aereo volando...'
class Camara:
    carga_disponible = 0
class Digital(Camara):
    resolucion = 0
    def __init__(self, res):
        self.resolucion = res
    def descargar_archivos(self):
        return 'archivos descargados de camara digital...'
class Analogica(Camara):
    numero_tomas = 0
    def imprimir(self):
        return 'imprimiendo...'
    
class Dron(Aereo, Digital):
    def __init__(self, altura, resolucion, alcance):
        super().__init__(altura)
        Digital.__init__(self, resolucion)
        self.alcance = 2000
        
    def volar(self):
        return str(super().volar())  + '\nEl dron esta volando'
    
    def descargar_archivos(self):
        return Digital.descargar_archivos(self)  + '\nEl dron esta descargando archivos ...'
    
if __name__ == '__main__':
    d1 = Dron(500, 8192, 1750)
    print (d1.volar())
    print (d1.descargar_archivos())
        