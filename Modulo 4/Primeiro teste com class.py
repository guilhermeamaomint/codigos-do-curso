class fichapersonagem:
    def __init__(self, nome: str, forc: int, proeficiencia: int, rolagem1: int, rolagem2: int):
        self.nome = nome 
        self.forc = forc 
        self.proeficiencia = proeficiencia 
        self.rolagem1 = rolagem1 
        self.rolagem2 = rolagem2 
        print(f"{self.nome} ataca rolando {self.rolagem1} no dado")
        print(f"Se a CA do seu inimigo é menor que {self.rolagem1+self.forc+self.proeficiencia} ele toma {self.rolagem2+self.forc}")

nome = input("Digite o nome do personagem: ")
forca = int(input("Digite o valor de força do personagem: "))
proeficiencia = int(input("Digite o valor de proeficiencia do personagem: "))
rolagem1 = int(input("Digite o valor do d20 para acertar: "))
rolagem2 = int(input("Digite o valor do dado de dano: "))

# personagem1 = fichapersonagem("Iccarion", "5", "5", "12", "40")
personagem1 = fichapersonagem(nome, forca, proeficiencia, rolagem1, rolagem2)
