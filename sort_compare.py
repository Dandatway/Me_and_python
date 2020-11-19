# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:47:29 2020

@author: Daniel
"""

lista=list(input('Introduce la lista: '))

for x in range(len(lista)):
    lista[x]=int(lista[x])

it = 0

while it <= len(lista)-3:
    for x in range(it+1, len(lista)):
        if lista[x-1] > lista[x]:
            value = lista[x]
            index_value = x
    lista.pop(index_value)
    lista.insert(it, value)
    it += 1
    print(lista)

