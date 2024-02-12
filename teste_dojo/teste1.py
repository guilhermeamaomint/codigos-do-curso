def convercao(numero):  
    if numero <= 3:
        return "I"*numero
    elif numero <= 5:
        return "I"
    elif numero % 10 == 0:
        repetir = int(numero/10)
        return "x"*repetir
numero = int(input("Digite o numero: "))
numero_romano= convercao(numero)
print("Numero em romano:1", numero_romano)