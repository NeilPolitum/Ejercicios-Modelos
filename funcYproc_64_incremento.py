numero = int(input("ingrese el numero a incrementar: "))
incre = int(input("Ingrese el incremento: "))
def incremento(num):
    num = num + incre
    return num
var = True
while var:
    l = int(input("¿Desea incrementar el numero? \n 0 = no \n 1 = si"))
    if l == 0:
        var = False
    elif l == 1:
        numero = incremento(numero)
        print(numero)
