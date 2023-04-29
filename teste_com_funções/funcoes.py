def coiso(nome, idade):
    print("oi", nome, "sua idade é", idade)

def soma_dois_numeros(primeiro, segundo):
    return primeiro + segundo

def potencia(x, expoente = 2):
    return x ** expoente

def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

def mistura_de_palavras(*args):
    return '_'.join(args)

def testez():
    numero = input("Digite um número para teste: ")
    return numero

def nome_do_guigo():
    varcontrole = False
    nome = input("digite guilherme: ")
    if nome == "guilherme":
        varcontrole = True
    print(f"o nome digitado foi: {nome}")
    return varcontrole

def soma_numeros(*args):
    soma = 0
    for numero in args:
        soma = soma + numero
    return soma

def nomes_lista():
    nomes = ['MARIA', 'JOÃO', 'ANA', 'PEDRO']
    varcontrole = False
    nome = input("digite seu nome: ").upper()
    if nome in nomes:
        varcontrole = True
    print(f"o nome digitado foi: {nome}")
    return varcontrole
def descricao_de_livro(titulo, autor="desconhecido"):
    print(f"o nome do livro é: {titulo}",f"o nome do autor do livro é {autor}", sep="\n")
