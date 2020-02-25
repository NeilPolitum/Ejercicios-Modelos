# -*- coding: utf-8 -*-
def potencia(num,exp):
    if exp == 0:
        return 1
    elif num < 0:
        return potencia(num, exp+1)/num
    elif exp > 0:
        return num*potencia(num, exp-1)
    
print("Bienvenido, este programa halla la potencia de un numero con recursividad")
num = int(input("Ingrese el numero: "))
exp = int(input("Ingrese el exponente: "))

print("El resultado es: "+str(potencia(num,exp)))