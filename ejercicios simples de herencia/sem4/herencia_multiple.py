class vehiculo:
    velocidad = 0
    nombre = ""

class Terrestre(vehiculo):
    def avanzar():
        'vehiculo terrestre avanzando...'
    
class Aereo(vehiculo):
    altura_max= 0
    def __init__(self, altura):
        self-altura_max = altura
    def volar():
        'vec¿hiculo aereo volando...'
class Camara:
    cargo_disponible = 0

class Digital(Camara):
    resolucion = 0
    def __init__(self,resolucion):
        self.resolucion = resolucion
    def descargar_archios():
        return 'archivo descargado de camara digital...'
class Analogica(Camara):
    numero_tomas=0
    def imprimir():
        return 'imprimiendo'

class Dron(Aereo, Digital):
    def __init__(self,altura,resolucion,alcance):
        super().__init__(altura)
        Digital.__init__(self,resolucion)
        self.alcance = 2000
        
    def volar(self):
        return super().volar(self) + '\n' + 'El dron esta volnado'
    
    def descargar_archios(self):
        return Digital.descargar_archios() + '\n' + 'El dron esta descargando archivos...'
    
if __name__ == '__main__':
    d1 = Dron(500, 81292, 1750)
    print(d1.volar())
    print(d1.descargar_archios())
