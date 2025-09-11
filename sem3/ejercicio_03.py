""""
    ejercicio_03
    fecha 11-09-2025
"""
import unittest

class Producto:
    def __init__(self, nombre:str, precio_unitario:float):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        

class ProductoElectronico(Producto):
    def Calcular_pago(self, cantidad:int) -> float:
        if cantidad > 5 :
            return super().Calcular_pago(cantidad) * 0.9
        else:
            return super().Calcular_pago(cantidad)

class ProductoAlimento(Producto):
    def __init__(self, nombre:str, precio_unitario:float, fecha_vencimiento:str):
        super().__init__(nombre, precio_unitario)
        self.fecha_vencimiento = fecha_vencimiento

#prueba
elect = ProductoElectronico('Parlante', 120)
print(elect.calcular_pago(6))
print(elect.calcular_pago(5))
    
alim=ProductoAlimento('Leche', 50, '2023-12-01')
print(alim.calcular_pago(6))
print(alim.calcular_pago(5)) 
print('vencimiento: ' + alim.fecha_vencimiento)