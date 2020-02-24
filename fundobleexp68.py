# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:53:28 2020

@author: danie
"""
import math

def operacion(x):
    op = math.pow(x,2)-(2*x)
    return op

x = int(input("Ingrese un numero: "))
print(operacion(x))