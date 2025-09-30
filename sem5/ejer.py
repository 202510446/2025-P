

class motor:
    def __init__(self, tipo_motor:str):
        self.tipo_motor = tipo_motor
    def monstrar_motor(self):
        return f'Tipo de motor: {self.tipo_motor}'
        
class ruedas:
    def __init__(self, cantidad_ruedas:int):
        self.cantidad_ruedas = cantidad_ruedas
        
    def mostrar_ruedas(self):
        return f'Cantidad de ruedas: {self.cantidad_ruedas}'

class Vehiculo(motor, ruedas):
    def __init__(self, tipo_motor:str, cantidad_ruedas:int,velociadad_maxima:int):
        super().__init__(tipo_motor, cantidad_ruedas, velociadad_maxima)
        motor.__init__(self, tipo_motor)
        ruedas.__init__(self, cantidad_ruedas)
        self.velocidad_maxima = velociadad_maxima
    def monstrar_info(self):
        print(self.monstrar_motor())
        print(self.mostrar_ruedas())
        print(f'Velocidad máxima: {self.velocidad_maxima} km/h')
    def probar(self, n):
        for km_h in range(0, n+1, 10):
            if km_h <= self.velocidad_maxima:
                print(f'El vehículo va a {km_h} km/h')
            else:
                print(f'El vehículo ha superado su velocidad máxima de {self.velocidad_maxima} km/h y se detiene.')
                break
#-------------#
def main():
    try:
        print("==== SIMULADOR DE VEHICULOS ====")
        tipo_motor = input("Ingrese el tipo de motor (gasilina, diésel,eléctrico): ")
        cantidad_ruedas = int(input("Ingrese la cantidad de ruedas: "))
        velocidad_maxima = int(input("Ingrese la velocidad máxima (km/h): "))
        vehiculo = Vehiculo(tipo_motor, cantidad_ruedas, velocidad_maxima)
        print("\nInformación del vehículo:")
        vehiculo.mostrar_info()
        n = int(input("Ingrese hasta que velocidad quierer probar el vehiculo: "))
        vehiculo.probar(n)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return 'Fin del programa'

if __name__ == "__main__":  
    main()