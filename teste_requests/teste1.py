def nome_do_guigo():
    varcontrole = False
    nome = input("digite guilherme: ")
    if nome == "guilherme":
        varcontrole = True
    print(f"o nome digitado foi: {nome}")
    return varcontrole
retorno = nome_do_guigo()
if retorno:
    print("parabéns, vc não é um imbecil")
else:
    print("imbecil")
