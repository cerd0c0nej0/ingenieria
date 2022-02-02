# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 16:43:37 2022

@author: LENOVO
"""
list = []
n = 1   #valores del 1 al 100
while n <= 100: #bucle de numeros de 1 al 100
    c = 1 # div
    x = 0 #contador div
    while c <= n:
        if n % c == 0: 
            x = x + 1
        c = c + 1
    if x == 2:
        list.append(n)       
    n = n + 1 # incrmeneto valor  
print(" los numeros primos del 1 al 100 son :",list)