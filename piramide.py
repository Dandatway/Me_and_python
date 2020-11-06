# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:03:01 2020

@author: Daniel
"""


cima=int(input('Ingresa un numero: '))

for x in range(1,cima+1):
    xstr=str(x)
    print(xstr*x)
    if x==cima:
        for y in range(cima-1,0,-1):
            ystr=str(y)
            print(ystr*y)
