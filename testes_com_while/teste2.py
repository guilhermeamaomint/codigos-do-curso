print("inicio")

soma = 0

contagem = 0

max_repeticoes = 1000

while soma < 100:
    soma -= 1
    contagem += 1
    print(f"soma = {soma}")
    if contagem == max_repeticoes:
        print(f"maximo de repetições {max_repeticoes} alcançado")
        break
print("fim")