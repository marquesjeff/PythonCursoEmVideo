print("Comparando Números!")

numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Segundo número: "))

if numero1 == numero2:
    print("Os valores são IGUAIS.")
elif numero1 > numero2:
    print(f"O valor {numero1} é MAIOR que o valor {numero2}")
else:
    print(f"O valor {numero2} é MAIOR que o valor {numero1}")