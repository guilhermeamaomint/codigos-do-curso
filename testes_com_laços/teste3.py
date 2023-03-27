nomes = ["ana", "MARIA", "JOaO", "Jose", "zeca", "Diego"]
idades = [20, 68, 25, 40, 60, 50]


for indice, idade in enumerate(idades):
    if idade > 50:
        print(f"indice:{indice} contem idade maior que 50")
print(idades[1], idades[4])
