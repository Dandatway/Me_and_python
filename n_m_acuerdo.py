# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:15:19 2020

@author: Daniel
"""


texto=input('Introduce el texto a analizar').upper()

abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for x in texto:
    if x in abc:
        print('El texto esta')
