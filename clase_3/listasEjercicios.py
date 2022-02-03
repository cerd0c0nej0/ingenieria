# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 20:02:44 2022

@author: LENOVO
"""

# 1.- dada la lista encontrar el mayor elemento

lista = [1,3,5,100]

# usando funcion max

print('el numero mayor de la lista es:',max(lista))

# 2.- dada la lista mostrar el promedio de los elementos

lista_2 = [1,3,4,6,7]

# usando numpy.mean
import numpy
print('el promedio de los elemento es:',numpy.mean(lista_2))

#usando la longitud de la lista

a = sum(lista_2)
b = len(lista_2)
prom=a/b
print('el promedio es :',prom)

    
