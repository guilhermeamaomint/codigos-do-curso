nomes = ["ana", "ptolomeu", "jesus", "Jose", "marcelo", "Diego"]
idades = [20, 68, 25, 40, 60, 50]

nomes_com_até_5_caract = []
for nome in nomes:
    if len(nome) <= 5:
        nomes_com_até_5_caract.append(nome)
        
print(nomes_com_até_5_caract)
print([nome.upper() for nome in nomes])
