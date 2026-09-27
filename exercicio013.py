print("Ajuste Salarial!")
salario = float(input("Qual o salário do funcionário? R$"))
aumento = salario * (15 / 100)
salarioFinal  = salario + aumento
print(f"O funcionário que recebia R${salario:.2f} ganhará um aumento de 15% e passará a receber R${salarioFinal:.2f}")
