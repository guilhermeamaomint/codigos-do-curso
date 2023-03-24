curso = ".format"
print("no curso eu aprendi que da pra usar o  {curso1}".format(
    curso1 = curso
))
fa = "f"  #não esquecer de colocar as aspas
print(f"o curso tbm me ensinou a usar o {fa}"
      )
#testando branches

valor_de_combustivel = 6.8994
litros = 20 
total_abastecido = valor_de_combustivel * litros

print(f"total: {total_abastecido:.2f} R$")
print("total: {:.2f} R$".format(total_abastecido))

print("vou contar de 1 a 10")
for i in range(10):
    valor = i + 1
    print(f"contando: {valor:2}")
