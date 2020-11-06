# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:47:45 2020

@author: Daniel
"""
#Clase de if else elif
value=int(input('Ingresa un numero entero: '))

if value < 5:
    print(f'El numero es menor a 5')
if value < 3:
    print(f'El numero es menor a 3')
elif value == 5:
    print(f'El numero es igual a 5')
else:
    print(f'El numero {value} es mayor a 5')