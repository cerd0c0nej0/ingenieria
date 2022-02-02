# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:00:37 2022

@author: LENOVO
"""
"""
def mi_funcion():
    print("hola mundo")
    
def returnHolaMundo:
    return "Hola Mundo"

#llamar funcion

mi_funcion()

#llamar a una funcion que retorna

hola_mundo = returnHolaMundo()
print(hola_mundo)
"""
#parametros de funciones

def mi_funcion_params(nombre, apellido):
    print (nombre, apellido)
    
#llamas a funcion que tiene parametros
mi_funcion_params('gabriela', 'ustariz')

def mi_funcion_Param (nombre, apellido):
    return f'{nombre} - {apellido}'
nombreApconGuion = mi_funcion_Param('gabriela','ustariz')
print(nombreApconGuion)

#como fue implementado el pop
def pop(lista,index=0):
    print(lista,index)

lista = [1,3,4]
#va a eliminar el ultimo elemento
lista.pop()
#elimina el elemnto con indice 0
lista,pop(0)

