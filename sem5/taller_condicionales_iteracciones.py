"""
    Objetivo:   Practicar con estructuras condicionales e iterativa
    Fecha:      23-09-2025    
"""
import random
#--------------#
# Ejercicio 01 #
#--------------#
def ejercicio_01():
    # Pedir un numero
    try:
        numero = int(input('Ingrese el número a comparar: '))
    except ValueError:
        return 'Debe ingresar un valor numérico'  # finaliza la función y devuelve el valor
    # Comparar si es mayor a 0
    if numero > 0:
        return 'El número es positivo'
    else:
        return 'el número es negativo o cero'
    # devolver el mensaje
#--------------#1
# Ejercicio 02 #
#--------------#
def ejercicio_02():
    try:
        num1 = int(input('Ingrese el número1 a comparar: '))
        num2 = int(input('Ingrese el número2 a comparar: '))
    except ValueError:
        return 'Debe ingresar un valor numérico'
    if num1 > num2:
        return f'El número {num1} es mayor que el número {num2}'
    elif num1 < num2:
        return f'El número {num2} es mayor que el número {num1}'
    else:
        return 'Los 2 números tienen el mismo valor'
#--------------#1
# Ejercicio 03 #
#--------------#
def ejercicio_03():
    # Pedir un numero
    try:
        numero = int(input('Ingrese el número: '))
    except ValueError:
        return 'Debe ingresar un valor numérico'  # finaliza la función y devuelve el valor
    # bloque iterativo para multiplicar
    mensaje = ''
    for nro in range(1, 13):
        mensaje += f'{numero} x {nro} = {numero * nro}\n'
    return mensaje
#--------------#1
# Ejercicio 06 #
#--------------#
def ejercicio_06():
    # Pedir un numero
    try:
        numero = int(input('Ingrese el número: '))
    except ValueError:
        return 'Debe ingresar un valor numérico'  # finaliza la función y devuelve el valor       
    digitos = 0
    if numero == 0:
        return 'Tiene 1 dígito'
    while numero != 0:
        numero = numero // 10
        digitos += 1
    return f'El número tiene {digitos} digitos'
#--------------#1
# Ejercicio 08 #
#--------------#
def ejercicio_08():
    # Pedir un numero
    try:
        numero = int(input('Ingrese el número: '))
    except ValueError:
        return 'Debe ingresar un valor numérico'  # finaliza la función y devuelve el valor
    # Es cero
    if numero == 0:
        return f'El factorial de {numero} es 1'
    fact = 1
    i = 1
    while i <= numero:
        fact *= i
        i += 1
    return f'El factorial de {numero} es {fact}'
#--------------#1
# Ejercicio 09 #
#--------------#
def ejercicio_09():
    # Pedir un numero
    try:
        numero = int(input('Ingrese para verficar si es primo: '))
    except ValueError:
        return 'Debe ingresar un valor numérico'  # finaliza la función y devuelve el valor
    es_primo = True
    if numero <= 1:
        return 'El número no es primo (0 o negativo)'
    for i in range(2, numero):
        if numero % i == 0:   # El residuo de dividr numero entre i es cero
            return 'El número no es primo'
    return 'El número es primo'

#--------------#1
# Ejercicio 10 #
#--------------#
def ejercicio_10():
    # Pedir un numero
    try:
        numero = int(input('Ingrese cuantos términos de la serie Fibonnaci se deben mostrar: '))
    except ValueError:
        return 'Debe ingresar un valor numérico'  # finaliza la función y devuelve el valor
    primero, segundo = 0, 1
    contador = 0
    linea = ''
    while contador < numero:
        linea += ' ' + str(primero)
        primero, segundo = segundo, primero + segundo
        contador += 1
    return linea
#--------------#1
# Ejercicio 12 #
#--------------#
def ejercicio_12(): 
    # Pedir un numero
    try:
        numero = int(input('Ingrese el número de día de la semana: '))
    except ValueError:
        return 'Debe ingresar un valor numérico'  # finaliza la función y devuelve el valor
    match numero:
        case 1:
            return 'Lunes'
        case 2:
            return 'Martes'
        case 3:
            return 'Miércoles'
        case 4:
            return 'Jueves'
        case 5:
            return 'Viernes'
        case 6:
            return 'Sábado'
        case 7:
            return 'Domingo'
        case _:
            return 'Debe ingresar un número entre 1 y 7'
#--------------#1
# Ejercicio 11 #
#--------------#
def ejercicio_11(): 
    # Generar un numero aleatorio
    secreto = random.randint(1, 20)
    intento = 0
    adivinado = False

    while not adivinado:
        # Pedir un numero
        try:
            numero = int(input('Ingrese el número a adivinar: '))
        except ValueError:
            return 'Debe ingresar un valor numérico'  # finaliza la función y devuelve el valor 
        intento += 1
        if numero == secreto:
            print (f'Correcto!!, adivinaste en {intento} intentos')
            adivinado = True
        elif numero < secreto:
            print('Demasiado bajo')
        else:
            print('Demasiado alto')
                            
#----------------#
# Menu principal #
#----------------#
def main():
    while True:
        print('\n=== condicionales e Iteraciones ===')
        print('1. Número positivo o negativo')
        print('2. Mayor de dos números')
        print('3. Tabla de multiplicar')
        print('6. Dígitos de un número')
        print('8. Factorial de un numero')
        print('9. Número primo')
        print('10. Serie Fibonacci')
        print('12. Día de la semana')
        print('0. Salir del sistema')
        
        # Aceptar un número por teclado
        opcion = int(input('Seleccione una opción: '))
        
        if opcion == 1:
            print(ejercicio_01())   # Imprime el valor que retorna
        elif opcion == 2:
            print(ejercicio_02())
        elif opcion == 3:
            print(ejercicio_03())
        elif opcion == 6:
            print(ejercicio_06())
        elif opcion == 8:
            print(ejercicio_08())
        elif opcion == 9:
            print(ejercicio_09())
        elif opcion == 10:
            print(ejercicio_10())
        elif opcion == 11:
            ejercicio_11()
        elif opcion == 12:
            print(ejercicio_12())
        elif opcion == 0:
            print('gracias por usar el sistema')
            break
        else:
            print('opción incorrecta, intente de nuevo')

if __name__ == '__main__':
    main() 