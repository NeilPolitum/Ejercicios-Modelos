# -*- coding: utf-8 -*-
import math

def operacion(x):
    op = math.pow(x,2)-(2*x)
    return op

x = int(input("Ingrese un numero: "))
print(operacion(x))