""""
Programa: ejercicio_02.py
fecha 09-09-2025
"""
class vehiculo:
    def __init__(self, marca:str,modelo:str):
        self.marca=marca
        self.modelo=modelo
        
    def mostrar_into(self) -> str:
        return f'Datos del vehiculo \n Marca: {self.marca}\n Modelo: {self.modelo}'
    
class Automovil(vehiculo):
    def __init__(self, marca: str, modelo:str,num_puertas:int):
        super().__init__(marca,modelo)
        self.num_puertas = num_puertas
        
    def es_deportivo(self) -> bool:
        return (self.num_puertas == 2)
    
#Prueba unitaria
class TestPruebaAutomovil(unittest.TestCase):
    def setup(self):
        self.auto1 =Automovil('Mazda','3',4)
        self.auto2 =Automovil('Ferrari','Z',2)

    def test_auto_no_deportivo(self):
        self.assertIsNot(self.auto1.es_deportivo())
        
    def test_auito_deportivo(self):
        self.asserTrue(self.auto2.es_deportivo())

    def test_auto_deportivo_2(self):
        self.assertno(self.auto2.es_deportivo()),True)
        
    def test_auto_deportivo_3(self):
        self.assertLess(self.auto2.num_puertas,3)
        
if __name__ == '__main__':
    # unittest.main()
    # Prueba clave automovil
    auto3= Automovil('Honda','Accord',2)
    if auto3.es_deportivo():
        print (auto3.mostrar_info() + '\n(Auto deportivo)')
    else:
        print (auto3.mostrar_info() + '\n(Auto sedan)')