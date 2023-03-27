nomes = ["ana", "MARIA", "JOaO", "Jose", "zeca", "Diego"]
for nome in nomes:
    nome = nome

idades = list(range(1, 7))
for id in idades:
    id = id

nums = []
for num in range(1, 7):
    num = (num*10)
    nums.append(num)

nomes_e_idades = zip(nomes, nums)

for nome3, idade3 in nomes_e_idades:
    print(f"{nome3.lower()} tem {idade3} anos")

