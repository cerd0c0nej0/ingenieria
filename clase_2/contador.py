# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:11:22 2022

@author: LENOVO
"""
"""
#contador de 1 en 1

cont=0
#cont +=1 
#contar numero del 1 al 10 y mostrar en pantalla
while cont<10:
    cont = cont + 1
    print (cont)
    
#sumar numeros del 1 al 10
 
n = 1
sum = 0

while n <=10:
    pass
    sum = sum + n
    n = n + 1

print (f'la suma total de 1 al 10 es {sum}')

#multiplicar del 1 al 10

m = 1 
prod = 1

while m <=10:
       pass
       prod = prod * m
       m = m + 1
print (f'el producto total de 1 al 10 es {prod}')

#modulo

for num in range (1,11):
    if num % 2 == 0:
        print ("numeros pares:", num)
  """ 
# crear lista

list=[1, 3, 4, 55, 4]

# contador elementos de una lista
 
c = 0
for elementos in list:
    c=c+1
print("la cantidad de elementos en la lista es:",c)
    
# numeros pares

for elementos in list:
    if elementos % 2 ==0:
        print("los numeros pares son:",elementos)

#numeros impares

for elementos in list:
    if elementos % 2 != 0:
        print("los numeros impares son : ",elementos)
        
s=0
sf=0
for elementos in list:
    s = s + elementos
    
sf=s
print("la suma es :",sf)

#producto

p=1
pf=0
for elementos in list:
    p = p*elementos
pf=p
print("el producto es:", pf) 


#ordenar de mayor a menor 

print("la lista ordenada de menor a mayor es:",sorted(list))

# ordenar de mayor a menor

print("la lista ordenada de mayor a menor es:",sorted(list, reverse=True)) 
       