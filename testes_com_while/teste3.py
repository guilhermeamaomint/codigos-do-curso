while True:
    try:
        num = int(input("Digite um número inteiro: "))
        print("O número digitado foi:", num)
        break
    except ValueError:
        print("Ops, isso não é um número inteiro válido! Tente novamente...")
#codigo gerado pelo chatgpt para eu compreender melhor o try/except