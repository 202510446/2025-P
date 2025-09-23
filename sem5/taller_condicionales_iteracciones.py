"""
    obejtivo: Practicar con estructuras condicionales e iterativa
    fecha: 23-09-2025
"""
#--------------#
# Ejercicio 01 #
#--------------#
def ejercicio_01():
    # Pedir un numero
    try:
        numero = int(input('Ingrese un numero a comparar: '))
    except ValueError:
        return 'Debe ingresar un valor numerico' # finalizar la funcion y devolver el valor
    # Comparar si es mayor a 0
    if numero > 0:
        return 'El numero es positivo'
    else:
        return 'El numero es negativo'
    # delvolver el mensaje
#--------------#
# Ejercicio 02 #
#--------------#
def ejercicio_02():
    try:
        num1 = int(input('Ingrese el numero 1 a comparar: '))
        num2 = int(input('Ingrese el numero 2 a comparar: '))
    except ValueError:
        return 'Debe ingresar un valor numerico'
    if num1 > num2:
        return f'El numero {num1} es mayor que el numero {num2}'
    elif num1 < num2:
        return f'El numero {num2} es mayor que el numero {num1}'
    else:
        return 'Los dos numeros tienen el mismo valor'
    
#--------------#
# ejercicio 03 #
#--------------#
def ejercicio_03():
    #pedir un numero
    try:
        numero = int(input('Ingrese un numero para ver su tabla de multiplicar: '))
    except ValueError:
        return 'Debe ingresar un valor numerico' # finalizar la funcion y devuelve el valor
    #bloque iterativo para multiplicar
    mensaje = ''
    for nro in range(1, 13):
        mensaje += f'{numero} X {nro} = {numero * nro}\n'
    return mensaje
#--------------#
# ejercicio 06 #
#--------------#
def ejercicio_06():
    #pedir un numero
    try:
        numero = int(input('Ingrese un numero: '))
    except ValueError:
        return 'Debe ingresar un valor numerico' # finalizar la funcion y devuelve el valor
    digitos = 0
    if numero == 0:
        return 'El numero tiene 1 digito'
    while numero != 0:
        numero = numero // 10  # division entera
        digitos += 1
    return f'El numero tiene {digitos} digitos'

#--------------#
# ejercicio 08 #
#--------------#
def ejercicio_08():
    #pedir un numero
    try:
        numero = int(input('Ingrese un numero:'))
    except ValueError:
        return 'Debe ingresar un valor numerico' # finalizar la funcion y devuelve el valor
    #es cero
    if numero == 0:
        return 'El factorial de {numero} es 1'
    fact = 1
    i=1
    while i<= numero:
        factorial *=i
        i += 1
    return f'El factorial de {numero} es {fact}'

#--------------#
# ejercicio 09 #
#--------------#

def ejercicio_09():
    #pedir un numero
    try:
        numero = int(input('Ingrese un numero para verificar si es primo: '))
    except ValueError:
        return 'Debe ingresar un valor numerico' # finalizar la funcion y devuelve el valor
    es_primo = True
    if numero <= 1:
        return 'El numero no es primo(0 o es negativo)'
    for i in range(2, numero):
        if numero % i == 0:   # el residuo es dividir numero entre i es cero
            return 'El numero no es primo'
    return 'El numero es primo'

#--------------#
# ejercicio 10 #
#--------------#
def ejercicio_10():
    #pedir un numero
    try:
        numero = int(input('Ingrese cuantos terminos de la serie de fibonacci desea ver: '))
    except ValueError:
        return 'Debe ingresar un valor numerico' # finalizar la funcion y devuelve el valor
    primero,segundo = 0,1
    contador = 0
    linea = ''
    while contador < numero:
        linea += '' + str(primero)
        primero ,segundo = segundo, primero + segundo
        contador += 1
    return linea

#--------------#
# ejercicio 12 #
#--------------#
def ejercicio_12():
    #pedir un numero
    try:
        numero = int(input('Ingrese el numero del dia de la semana: '))
    except ValueError:  
        return 'Debe ingresar un valor numerico' # finalizar la funcion y devuelve el valor
    match numero:
        case 1:
            return 'Lunes'
        case 2:
            return 'Martes'
        case 3:
            return 'Miercoles'
        case 4:
            return 'Jueves'
        case 5:
            return 'Viernes'
        case 6:
            return 'Sabado'
        case 7:
            return 'Domingo'
        case _:
            return 'Debe ingresar un numero entre 1 y 7'


#--------------#
# ejercicio 11 #
#--------------#
def ejercicio_11():
    #generar un numero aleatorio entre 1 y 20
    secreto = random.randint(1,20)
    intentos = 0
    adivinado = False
    
    while not adivinado:
        #pedir un numero
        try:
            numero = int(input('Adivine el numero a a divinar: '))
        except ValueError:
            return 'Debe ingresar un valor numerico' # finalizar la funcion y devuelve el valor
        intentos += 1
        if numero == secreto:
            print (f'Correcto!!, adivinaste en {intentos} intentos')
            adivinado = True
        elif numero < secreto:
            print('Demasiado bajo')
        elif:
            print('Demasiado alto')
#--------------#
#Menu Principal#
#--------------#
def main():
    while True:
        print('\n=== condicionales e Iteracciones ===')
        print('1. Numero positivo o negativo')
        print('2. Mayor de dos numeros')
        print('3. tabla de multiplicar')
        print('6. ejer 6')
        print('8. Factorial de un numero')
        print('9. Numero primo')
        print('10. Ejercicio 10')
        print('11. Ejercicio 11')
        print('12. Dia de la semana')
        print('0. Salir')
        
        # Aceptar un numero por teclado
        opcion = int(input('Seleccione una opcion: '))
        
        if opcion == 1:
            print(ejercicio_01()) # imprime el valor que retorna
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
            print(ejercicio_11())
        elif opcion == 12:
            print(ejercicio_12())
        elif opcion == 0:
            print('gracias por usar el sistema')
            break
        else:
            print('Opcion incorrecta, intente de nuevo')

if __name__ == '__main__':
    main()