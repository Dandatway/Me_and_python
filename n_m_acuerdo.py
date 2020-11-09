# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:15:19 2020

@author: Daniel
"""


text=input('Introduce el texto a analizar: ').upper()

abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a=''#string utilizado para comparar la secuencia alfabetica
b=''#string utilizado para guardar la secuencia alfabetica mas grande
pos_ant=0
for x in text:
    if x in abc:
        pos=abc.find(x)
        if pos >= pos_ant:
            if pos==pos_ant+1:
                pos_ant+=1
                a=a+x
            else:
                pos_ant=pos
                a=x
        else:
            pos_ant=0
            a=x
        if len(a)>len(b):
            b=a[:]
print(f'La secuencia de letras mas grande es. {b}')

