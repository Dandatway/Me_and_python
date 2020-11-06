# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:23:34 2020

@author: Daniel
"""

def get_bobs(tex=''):
    tex=tex.upper()
    bob='BOB'
    countin_bob=0
    count_for=0
    
    for letter in tex:
        if letter == bob[count_for]:
            count_for+=1
            if count_for==2:
                count_for=0
                countin_bob+=1
        else:
            count_for=0
        
    
    return f'En el texto hay {countin_bob} bobs'

variable1=input('Ingresa el texto:=')
string=get_bobs(variable1)
print(string)