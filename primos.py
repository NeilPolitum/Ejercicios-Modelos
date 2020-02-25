# -*- coding: utf-8 -*-
num = raw_input("Ingrese un numero >> ")
num = int(num)
contador = 0
verificar= False
for i in range(1,num+1):
    if (num% i)==0:
       contador = contador + 1
    if contador >= 3:
        verificar=True
        break

if contador==2 or verificar==False:
    print "El número es primo"
else: print "El número no es primo" 