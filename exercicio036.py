print("Empréstimo Aprovado!")

valor_casa = float(input("Informe o valor da casa: R$"))
salario = float(input("Informe seu salário: R$"))
anos_pagar = float(input("Em quantos anos pretende pagar?: "))
prestacao = valor_casa / (anos_pagar * 12)


print(f"Para financiar uma casa de R${valor_casa:.2f} o valor da prestação será de R${prestacao:.2f}")

if prestacao < salario * (30 / 100):
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO!")