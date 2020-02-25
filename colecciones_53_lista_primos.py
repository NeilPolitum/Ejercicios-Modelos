prueba = True
l = []
print("Este programa lista los numeros primos en un rango determinado: \n")
while prueba:
    n1 = int(input("Ingrese el limite INFERIOR de numeros en la lista: "))
    n2 = int(input("\nIngrese el limite SUPERIOR de numeros en la lista: "))
    if n1 > 1:
        for i in range(n1,n2):
            c = 2
            primo = True
            while primo and c < i:
                if i % c == 0:
                    primo = False
                else:
                    c += 1
            if primo:
                l.append(i)
        prueba = False
    else:
        print("incorrecto, ingrese numeros mayores a 1")
print("Lista de numeros primos")
print(l)
