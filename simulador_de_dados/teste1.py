import random as rd

quantidade = int(input("quantos dados vc quer rolar?: "))
total = 0
rolagem = 1
while rolagem <= quantidade:
    valor = rd.randint(1, 6)
    print(valor)
    rolagem += 1
    total = total + valor
print(f"O total é: {total}")
print(f"A media é: {total / quantidade}")
print("FIM DO PROGRAMA")
