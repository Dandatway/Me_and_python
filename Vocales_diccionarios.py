# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:15:38 2020

@author: Daniel
"""


#contador de vocales utilizando diccionarios

tex=input('Introduce un texto: ').upper()

vocales={
    'A':0,
    'E':0,
    'I':0,
    'O':0,
    'U':0
    }

count=0

for letter in tex:
    if letter =='A':
        vocales['A']+= 1
    elif letter =='E':
        vocales['E']+= 1
    elif letter =='I':
        vocales['I']+= 1
    elif letter =='O':
        vocales['O']+= 1
    elif letter =='U':
        vocales['U']+= 1

print(f'Estas son las vocales que tiene el texto')
print('vocales A: ', vocales['A'])
print('vocales E: ', vocales['E'])
print('vocales I: ', vocales['I'])
print('vocales O: ', vocales['O'])
print('vocales U: ', vocales['U'])