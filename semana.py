# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 08:39:21 2020

@author: danie
"""

array = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Bienvenido, estre programa recibe un número del 1 al 7, y devuelve el día de la semana "
      "respectivo")
dia=int(input("Ingrese un numero del 1 al 7: "))

while dia<1 or dia>7:
    dia = int(input("Ingrese un numero del 1 al 7: "))
    
print("El día es "+array[dia-1])