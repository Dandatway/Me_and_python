# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:03:01 2020

@author: Daniel
"""


n_max=int(input('Ingresa un numero: '))

for x in range(1,n_max):
    xstr=str(x)
    print(xstr*x)

for y in range(n_max,0,-1):
        ystr=str(y)
        print(ystr*y)
