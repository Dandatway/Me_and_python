# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:21:10 2020

@author: Daniel
"""
#Clase de for

"""times=int(input('Ingresa un numero entero: '))
for x in range(times):
    print(f'X {x}')
    if x >=10:
        print('Solo puedes iterar hasta el 10')
        break"""

lista=[]
for x in range(1, 50, 3):
    lista.append(x)
print(lista)
