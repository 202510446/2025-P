class CuentaBancaria:
    def __init__(self, numero_de_cuenta:str, saldo=float):
        self.numero_de_cuenta = numero_de_cuenta
        self.saldo = saldo
    def depositar(self, monto:float):
        if monto > 0:
            self.saldo += monto
    def consultar_saldo(self) -> float:
        return print(f'saldo',self.saldo)

    def retirar(self, monto:float):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
        else:
            return "error"
    
class CuentaAhorros(CuentaBancaria):
    def anula_retirar(self, monto,aplicar_cargo=False):
        if aplicar_cargo==True and monto > 50:
            tarifa_retiro = 2
            self.saldo -= tarifa_retiro
        if monto <= 0:
            return "error"

    def verificar_minimo_saldo(self,minimo):
        if self.saldo >= minimo:
            return True
        else:
            return False

class CuentaCorriente(CuentaBancaria):
    def anula_retirar(self, monto, aplicar_cargo=False):
        if aplicar_cargo==True and monto > 1000:
            tarifa_retiro = 0.01 * monto
        if monto <= 0:
            return "error"
    def aplicar_interes_negativo(self, tasa_interes:float):
        if self.saldo < 0:
            interes = abs(self.saldo) * (tasa_interes / 100)
            self.saldo -= interes
        return self.saldo
    
#prueba
if __name__ == '__main__':
    cuenta_ahorros = CuentaAhorros("123456", 500)
    cuenta_ahorros.depositar(200)
    cuenta_ahorros.consultar_saldo()  #saldo700
    cuenta_ahorros.retirar(100)
    cuenta_ahorros.consultar_saldo()  #saldo600
    cuenta_ahorros.anula_retirar(60, aplicar_cargo=True)
    cuenta_ahorros.consultar_saldo()  #saldo598
    print(cuenta_ahorros.verificar_minimo_saldo(500))  #true

    cuenta_corriente = CuentaCorriente("654321", -200)
    cuenta_corriente.depositar(300)
    cuenta_corriente.consultar_saldo()  #saldo100
    cuenta_corriente.retirar(50)
    cuenta_corriente.consultar_saldo()  #saldo50
    cuenta_corriente.anula_retirar(1500, aplicar_cargo=True)
    cuenta_corriente.consultar_saldo()  #saldo-15.0
    cuenta_corriente.aplicar_interes_negativo(5)
    cuenta_corriente.consultar_saldo()  #saldo-15.75