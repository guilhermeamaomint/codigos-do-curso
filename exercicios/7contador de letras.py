from funcoes import contaletra

letra = input("Digite a letra que tu quer contar: ")
frase = input("Digite a frase: ")
quantidade_letra = contaletra(frase, letra)

print(f"A letra '{letra}' aparece {quantidade_letra} vezes na frase.")