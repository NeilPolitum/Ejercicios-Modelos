# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:22:39 2020

@author: danie
"""

def suma(num1, num2):
	resultado = int(num1,2) + int(num2,2)
	return bin(resultado)

def resta(num1, num2):
	resultado = int(num1,2) - int(num2,2)
	return bin(resultado)

def multiplicacion(num1, num2):
	resultado = int(num1,2) * int(num2,2)
	return bin(resultado)

def division(num1, num2):
	resultado = int(num1,2) / int(num2,2)
	return bin(resultado)