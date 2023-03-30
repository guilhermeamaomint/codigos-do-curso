import random as rd
numero = rd.randint(1, 10)
tentativas = 5
while tentativas != 0:
    chute = int(input("digite seu chute: "))
    tentativas -= 1
    if numero == chute:
        print("Parabens, vc acertou!")
        break
    elif numero > chute:
        print("vc errou, o numero era maior")
    else:
        print("vc errou, o numero era menor")
print("FIM DO PROGRAMA")
