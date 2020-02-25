# -*- coding: utf-8 -*-
texto = raw_input("Ingrese la palabra que desea evaluar: ")

if str(texto) == str(texto[::-1]):
    print("Es palindroma")
else:
    print("No es palindroma")