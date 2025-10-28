"""
obejtivo: Introccion a la gestion de archivos de texto
Fecha: 23-10-2025
"""

# operacion de lectura
with open("datos.txt", "r", encoding="UTF-8") as archivo:
    contenido = archivo.read()
    print(contenido)
    
    archivo.close()
    
with open("datos.txt", "r", encoding="UTF-8") as archivo:
    distritos = []
    for linea in archivo:
        print(f'conteido linea: {linea.strip()}')
        parte = linea.strip().split(",")
        print('{'+ f'codigo: {parte[0]}, nombre: {parte[1]}'+'}')
        distritos.append({'codigo': parte[0], 'nombre': parte[1]})
        
    archivo.close()
    
    print(distritos)
    numero= int(input("ingrese un numero: "))
    for i in range (len(distritos)):
        if numero == distritos[1]['codigo']:
            print(f'El distrito es: {distritos[i]["nombre"]}')
    
    