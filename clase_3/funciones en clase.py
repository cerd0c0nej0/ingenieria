# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:17:23 2022

@author: LENOVO
"""

def funcion_1():
    print('hello')
    
def funcion_2():
    print("hello world")

funcion_1()
funcion_2()

#implementar pop
#dado una lista [2,3,4,9] implementar pop(lista)[2,3,4]
#no usasr lista.pop()

lista=[2,3,4,9]
def pop(lista):
    def pop(listaaux):
        listaaux = pop(lista)
        print({listaaux})
        
        
        
        
    