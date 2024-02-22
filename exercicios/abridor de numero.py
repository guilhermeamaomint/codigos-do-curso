def abertura(numero):
    if numero == 1:
        return 1
    return numero * abertura(numero - 1)

#numero = int(input("Digite um numero inteiro: "))
nmr = abertura(input("Digite um numero: "))