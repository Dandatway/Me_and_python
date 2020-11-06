# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:18:09 2020

@author: Daniel
"""


#contador de vocales

tex=input('Introduce un texto: ').upper()

vocales=['A','E','I','O','U']

count=0

for letter in tex:
    if letter in vocales:
        count += 1
    else:
        count =count

if count==1:
    print(f'El texto {tex} tiene {count} vocal')
else:
    print(f'El texto {tex} tiene {count} vocales')

