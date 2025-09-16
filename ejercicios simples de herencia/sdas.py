class profesional:
    def __init__(self,nombre:str,experiencia_años:int):
        self.nombre=nombre
        self.experiencia_años=experiencia_años
        
    def evaluar_desempeño():
        return ("Evalucion generica de desenpeño")
    
class ingeniero(profesional):
    def __init__(self, nombre: str, experiencia_años: int):
        if experiencia_años < 1:
            experiencia_años = 1
        super().__init__(nombre, experiencia_años)
    def evaluar_desempeño(self):
        if self.experiencia_años < 5:
            return ("Desempeño aexcelente, bono de 1000") 
        elif 2 < self.experiencia_años <= 5:
            return ("Desempeño bueno, bono de 500")
        else:
            return ("Desempeño regular, sin bonificacion")


    
class diseñador (profesional):
    def __ini__(self, nombre: str, experiencia_años: int):
        if experiencia_años < 0:
            experiencia_años = 0
        super().__init__(nombre, experiencia_años)
    def evaluar_desempeño(self):
        if self.experiencia_años > 7:
            return ("Desempeño excepcional, bono de 1500") 
        elif 3 > self.experiencia_años <= 7:
            return ("Desempeño muy bueno, bono de 750")
        elif 0 < self.experiencia_años <= 3:
            return ("En desarrollo, bono de 200")
        else:
            return ("Pricipiante, sin bonoficacion")

if __name__ == '__main__':
    ingeniero1 = ingeniero("Juan", 6)
    print(ingeniero1.evaluar_desempeño()) 

    diseñador1 = diseñador("Ana", 4)
    print(diseñador1.evaluar_desempeño()) 