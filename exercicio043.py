print("Índice de Massa Corporal!")

peso = float(input("Peso em Kg: "))
altura = float(input("Altura em m: "))
imc = peso / (altura ** 2)

print(f"Seu IMC é de {imc:.1f}")

if imc < 18.5:
    print("Status: Abaixo do Peso!")
elif imc < 25:
    print("Status: Peso Ideal!")
elif imc < 30:
    print("Status: Sobrepeso!")
elif imc < 40:
    print("Status: Obesidade!")
else:
    print("Status: Obesidade Mórbida!")