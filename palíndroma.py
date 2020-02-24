# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:12:50 2020

@author: danie
"""

texto = raw_input("Ingrese la palabra que desea evaluar: ")

if str(texto) == str(texto[::-1]):
    print("Es palindroma")
else:
    print("No es palindroma")