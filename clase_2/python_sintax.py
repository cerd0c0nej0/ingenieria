# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 07:18:50 2022

@author: LENOVO
"""
#comentario en linea 
"""
comentario en bloques o multilinea
linea 1
linea 2
"""
"""
#crear una constante
NAME = 'Gabriela'
FULL_NAME = 'Gabriela Isabel Ustariz Salinas'
print (NAME)
print (FULL_NAME)

#tipos de datos
entero = 90
print (f'el entero tiene valor de {entero}')
decimal = 6.14
print (f'en valor del decimal es {decimal}')
caracter = 'g'
print (f'en valor del decimal es {caracter}')
cadena = 'primera cadena'
print (f'en valor del decimal es {cadena}')
cadena_2 = "segunda cadena"
print (f'en valor del decimal es {cadena_2}')
booleano = False # valores true o false
print (f'en valor del decimal es {booleano}')
 
#lista
list = [1, 2, 3, 4]
print (f'en valor del decimal es {list}')

#diccionario
diccionario = {'nombre': 'gabriela isabel', 'edad': 30}
nombre = diccionario ["nombre"]
edad = diccionario ["edad"]

# entradas estandar
telefono = input("ingrese el numero de telefono")
print (f'el usuario ingreso ===> {telefono}:{edad}')
print("el resultado de la entrada es ", telefono)

#cast tipos

a = int(input("ingrese a :"))
b = int(input("ingrese b :"))

print(f' a+b es {a+b}')
"""

#estructura de control
año = 2001

if año <= 2022:
    print("año es menor a 2022")
elif año >= 1989:
    print("año es mayor a 1989")
else:
    print("no cumple con el rango de 1989 a 2022")
    