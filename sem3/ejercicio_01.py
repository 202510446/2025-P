""""
    ejercicio_01
    fecha 11-09-2025
"""
import unittest

class Empleado:
    def __init__(self, nombre:str,edad:int, salario:float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def calcular_bono(self):
        return self.salario * 0.1

class Gerente(Empleado):
    def __init__(self, nombre:str,edad:int, salario:float, departamento:str):
        super().__init__(nombre,edad,salario)
        self.departamento = departamento
        
    def calcular_bono(self):
        return self.salario * 0.2
    
    
class TestEmpleado(unittest.TestCase):
    def setUp(self):
        self.emp01=Empleado ('Juan',35, 3000)
        self.ger01=Gerente  ('Mari',33,5000,'Finanzas')
                             
    def test_compara_salarios(self):
        self.assertLess(self.emp01.salario,self.ger01.salario)
    
    def test_compara_bono(self):
        self.assertEqual(self.emp01.calcular_bono(),300)
        self.assertEqual(self.ger01.calcular_bono(),1000)
        
    def test_nombre(self):
        self.assertTrue(len(self.ger01.nombre) > len(self.emp01.nombre))
        
if __name__ == '__main__':
    unittest.main()