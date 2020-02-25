import random
j, k = 0, 1
print("Este programa llena una lista de manera aleatoria y la ordena")
#Pregunto la longitud del vector
longi = int(input("Ingrese el tamaño de la lista:  "))
n=int(longi)
a=[]
aux=n

i=0
#lleno el vector
while i < n:
    a.append(random.randint(1,100))
    i+=1
print("Lista aleatoria: \n")
print(a)
def burbuja(a):
    #ordeno
    j=0
    while j < n-1:
        k=j+1
        print(a)
        while k < n:
            if a[j] > a[k]:
                t = a[j]
                a[j] = a[k]
                a[k] = t
            k=k+1
            print(a)
        j=j+1
    print(a)

def seleccion(a):
    #Ordeno el vector
    i=0
    while i < n-1:
        j=i+1
        donde = i+1
        print(a)
        while j < n:
            if vector[donde] > vector[j]:
                donde = j
            j=j+1
            print(a)
        if vector[i] > vector[donde]:
            aux = vector[i]
            vector[i] = vector[donde]
            vector[donde] = aux
        i=i+1
        print(a)
    print(a)
    
def insercion(a):
    i = 1
    while i < n:
        print(a)
        j = i - 1
        t = a[i]
        while j >= 0 and a[j] > t:
            print(a)
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = t
        i += 1
    print(a)
    
def quicksort(a):
    izquierda = []
    centro = []
    derecha = []
    if len(a) > 1:
        pivote = a[0]
        for i in a:
            print(a)
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return sort(izquierda)+centro+sort(derecha)
    else:
      return a
    
print("\n4 opciones de ordenamiento de la lista")
l = int(input("Ingrese una opcion: \n1:Insercion \n2:Burbuja \n3:Seleccion \n4.QuickSort: "))
if l == 1:
    insercion(a)
elif l == 2:
    burbuja(a)
elif l == 3:
    seleccion(a)
elif l == 4:
    print(quicksort(a))

