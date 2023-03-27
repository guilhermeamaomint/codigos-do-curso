pode_parcelar = True
valor = 1500
limite = 1400

if (pode_parcelar or valor < 2000) and limite >= valor:
    print("posso comprar")
else:
    print("putz, ainda não posso comprar")
