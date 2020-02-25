def suma(x):
    if x == 0:
        return 0
    else:
        return x + suma(x-1)
print("Este programa realiza la suma de los primeros n numeros:")
l = int(input("Ingrese el n: "))
print(suma(l))
