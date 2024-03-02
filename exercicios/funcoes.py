# 1 par ou impar
def parimpar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

# 2 abridor de numero
def abrir(numero): #versão normal
    for i in range(numero, -1, -1):
        print(i, end="")

def abrirrecursivo(numero):
    if numero < 0:
        return
    print(numero, end="")
    abrirrecursivo(numero - 1)

# 3 soma de tres numeros
def somatres(a, b, c):
    return a + b + c

# 4 soma total # Duas funções pro mesmo programa 
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

def positivonegativozero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Zero"
