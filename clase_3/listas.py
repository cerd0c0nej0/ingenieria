# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 07:13:58 2022

@author: LENOVO
"""
#lista en blanco
lista = []

#lista con elementos
lista2 = [1,2,3,4,5]

#Acceder a elementos de una lista
listAlumnos = ["juan", "luis", "pablo"]
alumnospos_1 = listAlumnos[1]   #Hay 3 elementos y solo se puede elegir pero en este metodo se puede elegir la posicion de todos menos el ultimo

#para sacar elultimo elementos de la lista es:
alumnospos_2 = listAlumnos[len(listAlumnos)-1]
tamanioLista = len(listAlumnos)  #nos muestra el tamaño de la lista
print(alumnospos_1)
print(alumnospos_2)
print(tamanioLista)

#Insertar elementos a una lista
lista.append(1)
lista.append(2)          #lista [1,2,5]
lista.append(5)

#insertar un elemento en un indice de la lista - insert(indice(0, tamanio-1), elemento)
lista.insert(2, 3)   #index=indice
print(lista)

#eliminar elementos de una lista - lista[1,2,3,5]
lista.pop()
print(lista) #ahora la lista queda asi [1,2,3]; solo quita el ultimo

lista.pop(0)    #quita la primera, el 0 representa el primer - lista=[2,3]
print(lista)

#ahora con nombres
listaDocentes = ['juan', 'pablo', 'luis']
listaDocentes.remove('pablo')
print(listaDocentes)

#iterar listas = los pone en un orden a manera de tratar primero con juan y luego abajotrara con pablo, etc
listaDocentes2 = ['juan', 'pablo', 'luis', 'jaco']
for docente in listaDocentes2:
    print(docente)
    
#otra forma de iterar
tamaniolistaDocentes2 = len(listaDocentes2)
for i in range (0, tamaniolistaDocentes2):
    print(i)
