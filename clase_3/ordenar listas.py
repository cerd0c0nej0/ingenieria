# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 07:27:18 2022

@author: LENOVO
"""

 # i, j     ->  recordar que lo hara de 2 en 2, por eso definimos i, j
A = [55,86,32,12,82,43]  
print (A)
          # i, j  
          
#quiero ordenarlo de menor a mayor
    #1ero obtenemos el tamaño de la lista
num = len(A)
i=0
while i < num:
    j=i
    while j<num:
        if(A[i] > A[j]):
            #usaremos el metodo del swap, que intercambia valores
            aux=A[i]    #Usara un auxiliar para mover los elementos, osea seera un 3er cajon
            A[i]=A[j]             # i     j
            A[j]=aux                # aux
        j=j+1
    i=i+1
print ("Lista Ordenada")
print (A)

#forma de ordenarlo directo
listdeNumeros2 = [34,12,4,10]
print ("Lista Original")
print (listdeNumeros2)
listdeNumeros2.sort()
print ("Lista ordenada")
print (listdeNumeros2)

