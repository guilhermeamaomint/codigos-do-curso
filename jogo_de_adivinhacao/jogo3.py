import random as rd

numero = rd.randint(1, 3)

chute = int(input("digite seu chute: "))

if numero == chute:
    print("Parabens, vc acertou!")
elif numero > chute:
    print("vc errou, o numero era maior")
else:
    print("vc errou, o numero era menor")
print("FIM DO PROGRAMA")
