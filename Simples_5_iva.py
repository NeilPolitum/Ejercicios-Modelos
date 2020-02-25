def iva(valor):
    iva = valor*0.16
    return iva
print("Este programa calcula el iva de un producto dado su valor de venta:\n")
valor = int(input("Ingrese el valor del producto"))
print("El valor del iva es: " + str(float(iva(valor))) + "\nY el preciofinal del producto es: " + str(float(valor+iva(valor))))
