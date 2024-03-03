from funcoes import abrir
from funcoes import abrirrecursivo

versao = int(input("Voce quer usar a versão normal ou recursiva? (Normal = 1 e Recursiva = 2) "))

if versao == 1:
    numero = int(input("Digite um número inteiro: "))
    abrir(numero)
elif versao == 2:
    numero = int(input("Digite um número inteiro: "))
    abrirrecursivo(numero)
else:
    print("Você digitou errado se pa, digite apenas 1 ou 2 da proxima vez.")