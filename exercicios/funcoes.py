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

def somatotal(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

def vapo():
    numeros = []
    while True:
        numero = int(input("Digite um número inteiro (ou -1 para parar): "))
        if numero == -1:
            break
        numeros.append(numero)
    resultado = somatotal(*numeros)
    print("A soma de todos os números é:", resultado)