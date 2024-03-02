from funcoes import calculogorjeta

valor_conta = float(input("Digite o valor da conta do restaurante: "))
taxa_servico = float(input("Digite o percentual da taxa de serviço: "))
gorjeta = calculogorjeta(valor_conta, taxa_servico)

print(f"A gorjeta do garçom é: R${gorjeta:.2f}")