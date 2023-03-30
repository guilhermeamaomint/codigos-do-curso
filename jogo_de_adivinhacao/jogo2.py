import random as rd

numero = rd.randint(1, 3)

chute = int(input("digite seu chute: "))

if numero == chute:
    print("Parabens, vc acertou!")
else:
    print(f"Q pena, vc errou. O numero era {numero}")
print("FIM DO PROGRAMA")
