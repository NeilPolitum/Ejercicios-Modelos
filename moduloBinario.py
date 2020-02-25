# -*- coding: utf-8 -*-
import operacionesBinario

print("Bienvenido, este programa utiliza un modulo para hacer operaciones aritméticas entre numeros binarios")
numero1 = raw_input("Ingresar el primer numero binario: ")
numero2 = raw_input("Ingresar el segundo numero binario: ")

op=1
while op!=0:
    print("¿Qué desea hacer?\n"
          "1. Sumar\n"
          "2. Restar\n"
          "3. Multiplicar\n"
          "4. Dividir\n"
          "0. Salir\n")
    op = int(input()) 
    
    if op == 1:
        print(operacionesBinario.suma(numero1, numero2))
    elif op == 2:
        print(operacionesBinario.resta(numero1, numero2))
    elif op == 3:
        print(operacionesBinario.multiplicacion(numero1, numero2))
    elif op == 4:
        print(operacionesBinario.division(numero1, numero2))