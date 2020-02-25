# -*- coding: utf-8 -*-
import operacionesEnteros

print("Bienvenido, este programa utiliza un modulo para hacer operaciones aritméticas entre numeros binarios")
numero1 = raw_input("Ingresar el primer numero: ")
numero2 = raw_input("Ingresar el segundo numero: ")

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
        print(operacionesEnteros.suma(numero1, numero2))
    elif op == 2:
        print(operacionesEnteros.resta(numero1, numero2))
    elif op == 3:
        print(operacionesEnteros.multiplicacion(numero1, numero2))
    elif op == 4:
        print(operacionesEnteros.division(numero1, numero2))