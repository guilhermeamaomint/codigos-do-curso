def parimpar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

def abrir(numero): #versão normal
    for i in range(numero, -1, -1):
        print(i, end="")

def somatres(a, b, c):
    return a + b + c
