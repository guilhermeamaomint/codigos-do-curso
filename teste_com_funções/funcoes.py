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
