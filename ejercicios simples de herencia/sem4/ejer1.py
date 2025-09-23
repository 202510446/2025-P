
"""
    Ejercicio 1:: herencia multiple en empleado
    fecha: 18-09-2025
    semana: 4
"""
import unittest

class empleado:
    def __init__(self, nombre:str, salario_base:float):
        self.nombre = nombre
        self.salario_base = salario_base
    def calcular_salario(self)->float:
        return self.salario_base
    def mostrar_info(self)->str:
        return f'Nombre: {self.nombre}\nSalario Base: {self.salario_base}'

#emp1=empleado('Juan', 2000)
#dato=emp1.mostrar_info()
#print(dato)        
class trabajador(empleado):
    def __init__(self, nombre:str, salario_base:float,horas_extra:int,pago_hora:float):
        super().__init__(nombre, salario_base)
        self.horas_extra = horas_extra
        self.pago_hora = pago_hora
    def calcular_salario(self):
        return super().calcular_salario() + (self.horas_extra * self.pago_hora)
    def mostrar_info(self):
        return super().mostrar_info() + f',Horas Extra: {self.horas_extra}\nPago por Hora Extra: {self.pago_hora}'
#trb1=trabajador('Juan', 2000, 20, 15)
#dato=trb1.mostrar_info()
#print(dato)
#print(trb1.calcular_salario())
    
    
class gerente(empleado):
    def __init__(self, nombre:str, salario_base:float, bono:str):
        super().__init__(nombre, salario_base)
        self.bono = bono
    def calcular_salario(self):
        return super().calcular_salario() + self.bono
    def mostrar_info(self):
        return super().mostrar_info() + f',Bono: {self.bono}'
    
class MienbroSindicato: 
    def __init__(self,sindicato:str):
        self.sindicato = sindicato    
    def mostrar_info_sindicato(self)->str:
        return self.sindicato
    
    
class trabajadorSindicalizado(trabajador, MienbroSindicato):
    def __init__(self, nombre:str, salario_base:float,horas_extra:int,pago_hora:float,sindicato:str):
        super().__init__(nombre, salario_base, horas_extra, pago_hora)
        MienbroSindicato.__init__(self, sindicato)
    def mostrar_info(self)->str:
        return super().mostrar_info() + f',Sindicato: {self.mostrar_info_sindicato()}'

class GerenteSindicalizado(gerente, MienbroSindicato):
    def __init__(self, nombre:str, salario_base:float, bono:float,sindicato:str):
        super().__init__(nombre, salario_base, bono)
        MienbroSindicato.__init__(self, sindicato)
    def mostrar_info(self):
        return super().mostrar_info() + f',Sindicato en {MienbroSindicato.mostrar_info_sindicato()}'
    
class TestPruebaEmpleadosHerencia(unittest.TestCase):
    def setUp(self):
        ms = MienbroSindicato('Sindicato BCP')
        tr = trabajador('Juan', 2000, 200, 25)
        gr = gerente('Maria', 3000, 1000)
        trs = trabajadorSindicalizado('Jose', 2200, 20, 15, 'Sindicato Oficial')
        self.grs = GerenteSindicalizado('Ana', 2500, 500, 'Unidad Sindicato BCP')
        self.lista =[self.ms.
    def test_texto_sindicato(self):
        self.assertTrue('Sindicato' in self.ms.mostrar_menbresia())
    def test_salario_trabajador(self):
        self.assertGreater(self.tr.calcular_salario(), self.tr.salario_base)
    def test_salario_gerente(self):
        self.assertEqual(self.gr.calcular_salario(), (self.gr.salario_base + self.gr.bono))
    def test_diferencia_sindicato(self):
        self.assertNotEqual(self.trs.sindicato, self.grs.sindicato)
    def test_sindicato_en_lista(self):
        self.assertIn(self.trs.sindicato,['unidad sindical URP', 'Sindicato BCP','Sindicato Oficial'])
    def test_compara_numero_elelemento_en_lista(self):
        self.assertEqual(len(self.grs.mostrar_info().split(',')), 4)
        
if __name__ == '__main__':
    unittest.main()