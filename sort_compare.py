# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:47:29 2020

@author: Daniel
"""

lista=list(input('Introduce la lista: '))

for x in range(len(lista)):
    lista[x]=int(lista[x])

it=0

while it<=len(lista)-2:
    for x in range(it+1,len(lista)):
        if lista[x-1] > lista[x]:
            b=lista[x]
    lista.remove(b)
    lista.insert(it,b)
    it+=1
    print(lista)

