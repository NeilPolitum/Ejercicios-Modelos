# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 08:51:53 2020

@author: danie
"""

print("Bienvenido, este programa llena una lista con los 20 primeros numeros pares, y calcula "
      "la suma\n")

pares = range(20)
aux = 0
par = 0

while aux < 20:
    if(par%2==0):
        pares[aux] = par
        aux+=1
    par+=1
    
sum=0
for i in pares:
    sum+=i
    print(i)
    
print("La suma de los numeros pares es: "+str(sum))