from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_salario(self) -> float:
        return self.salario_base
        
    def mostrar_informacion(self):
        print (f'Empleado: {self.nombre} | Salario base: {self.salario_base}')
        
if __name__ == '__main__':
    obj = Empleado('Juan', 1000)
    obj.mostrar_informacion()