

print("Múltiplos aumentos!")

salario = float(input("Informe o salário do funcionário R$"))
salario_final = 0

if salario > 1250.00:
    aumento = salario * (10 / 100)
    salario_final = salario + aumento
    print(f"Quem ganhava R${salario:.2f} terá um aumento de 10% e passará a ganhar R${salario_final:.2f}")
else:
    aumento = salario * (15 / 100)
    salario_final = salario + aumento
    print(f"Quem ganhava R${salario:.2f} terá um aumento de 15% e passará a ganhar R${salario_final:.2f}")