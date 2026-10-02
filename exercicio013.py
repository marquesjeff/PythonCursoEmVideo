print("Ajuste Salarial!")
salario = float(input("Qual o salário do funcionário? R$"))
aumento = salario * (15 / 100)
salario_final  = salario + aumento
print(f"O funcionário que recebia R${salario:.2f} ganhará um aumento de 15% e passará a receber R${salario_final:.2f}")
