numero = 0
while numero <= 1000:
    if numero % 2 != 0:
        numero += 1
        continue
    print(f"o numero {numero} é par")
    
    if numero == 10:
        print("Ops... Ja verifiquei muitos numeros pares")
        break
    numero += 1
