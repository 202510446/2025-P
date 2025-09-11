""""
    ejercicio_02
    fecha 11-09-2025
"""

import unittest

class Vehiculo:
    def __init__(self,marca:str,modelo:str,velocidad_max:int):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        
    def detalles(self) -> str:
        return f"Datos del vehiculo:\n\tMarca: {self.marca}\n\tModelo: {self.modelo}\n\tVelocidad maxima: {self.velocidad_max} km/h" 
    
class Automovil(Vehiculo):
    def __init__(self,marca:str,modelo:str,velocidad_max:int, num_puertas:int):
        super().__init__(marca,modelo,velocidad_max)
        self.num_puertas = num_puertas

class Motocicleta(Vehiculo):
    def __init__(self,marca:str,modelo:str,velocidad_max:int, tipo:str):
        super().__init__(marca,modelo,tipo)
        self.tipo = tipo

if __name__ == '__main__':
    auto=Automovil('Fiat','5',150,2)
    print(auto.detalles() + f',mi auto tiene {auto.num_puertas} puertas')
    moto=Motocicleta('Susuki','Ninja ',140,'dportiva')
    print(moto.detalles() + f',mi moto es de tipo {moto.tipo}')
    
class TestVehiculo(unittest.TestCase):
    def setUp(self):
        self.auto = Automovil('Mazda', '6', 200,4)
        self.moto = Motocicleta('Honda', 'RX5', 180, 'deportiva')
        
    def test_compara_velocidades(self):
        self.assertGreater(auto.velocidad_max, moto.velocidad_max)
    
    def test_compara_longitu_marca(self):
        self.assertEqual(len(auto.marca), len(moto.marca))
        
if  __name__ == '__main__':
    unittest.main() 