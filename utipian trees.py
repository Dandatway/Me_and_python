# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:40:02 2020

@author: Daniel
"""

num_arboles=int(input('Cuantos arboles quieres testear: '))

for x in range(1 , num_arboles+1):
    ciclos=0
    altura=1
    ciclos=int(input(f'Cuantos ciclos son para el arbol {x}: '))
    while ciclos>0:
        ciclos-=1
        altura=altura*2
        if ciclos > 0:
            ciclos-=1
            altura+=1
    print(f'La altura del arbol {x} es de {altura} m')
