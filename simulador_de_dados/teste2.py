import random as rd

quantidade = int(input("quantos dados vc quer rolar?: "))
valores = []
rolagem = 1
while rolagem <= quantidade:
    valor = rd.randint(1, 6)
    valores.append(valor)
    rolagem += 1
print(valores)
print("o total é:", sum(valores))
print("a media é:", sum(valores) / quantidade)
print("maior: ", max(valores))
print("menor: ", min(valores))
print("FIM DO PROGRAMA")
