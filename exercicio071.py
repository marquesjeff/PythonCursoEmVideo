print("Simulador de Caixa Eletrônico")

print("-" * 20)
print("Banco Mundial")
print("-" * 20)

valor = int(input("Qual valor deseja sacar: R$"))

cedula = 50

while True:
    quantidade = valor // cedula

    if quantidade > 0:
        print(f"Total de {quantidade} cédulas de R${cedula:.2f}.")

    valor %= cedula

    if valor == 0:
        break

    if cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 5
    else:
        cedula = 1

print("Volte sempre!")