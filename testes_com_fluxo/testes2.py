import random as rd
d20 = rd.randint(1,20)
if d20 == 1:
    print("o player tirou uma falha critica")
elif 1 < d20 < 11:
    print("o player tirou uma falha")
elif 10 < d20 < 20:
    print("o player tirou um acerto")
else:
    print("O PLAYER TIROU UM 20!!!! MINHA NOSSA")
print(f"o numero tirado no d20 foi {d20}")
#jogar rpg é mais simples doq parece