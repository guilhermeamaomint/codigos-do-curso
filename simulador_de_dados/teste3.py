import random as rd

quantidade = int(input("quantos dados vc quer rolar? "))
valores = []
rolagem = 1
while rolagem <= quantidade:
    valor = rd.randint(1, 2)
    valores.append(valor)
    rolagem += 1
if rolagem == 1:
    print("jogar lol")
else:
    print("não jogar lol")