# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:44:43 2020

@author: Daniel
"""

#algoritmmo de burbuja

lista=list(input('Introduce la lista: '))

for x in range(len(lista)):
    lista[x]=int(lista[x])

estado=0

while estado<=len(lista):
    for x in range(1,len(lista)):
        if lista[x-1] > lista[x]:
            b=lista[x-1]
            lista[x-1]=lista[x]
            lista[x]=b
            estado=0
        else:
            estado+=1
        print(lista)
print(lista)