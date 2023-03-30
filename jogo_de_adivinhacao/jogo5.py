import random as rd
numero = rd.randint(1, 100)
tentativas = 10
while tentativas != 0:
    chute = int(input("digite seu chute: "))
    tentativas -= 1
    diferenca = numero - chute
    if diferenca == 0:
        print("Parabens, vc acertou!")
        break
    elif diferenca <= 5 and diferenca >= -5:
        print("vc errou, mas esta perto")
    elif diferenca > 0:
        print("vc errou, o numero era maior")
    else:
        print("vc errou, o numero era menor")
print(numero)
print("FIM DO PROGRAMA")
