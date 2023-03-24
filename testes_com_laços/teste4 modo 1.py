nomes = ["ana", "ptolomeu", "jesus", "Jose", "marcelo", "Diego"]
idades = [20, 68, 25, 40, 60, 50]

nomes_com_até_5_caract = [nome for nome in nomes if len(nome) <= 5]
print(nomes_com_até_5_caract)