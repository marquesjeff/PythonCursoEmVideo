print("Maior e menor valor!")

num1 = int(input("Primeiro Valor: "))
num2 = int(input("Segundo Valor: "))
num3 = int(input("Terceiro Valor: "))

menor_valor = num1
maior_valor = num1

if num2 > maior_valor:
    maior_valor = num2

if num3 > maior_valor:
    maior_valor = num3

if num2 < menor_valor:
    menor_valor = num2

if num3 < menor_valor:
    menor_valor = num3

print(f"O maior valor foi {maior_valor}")
print(f"O menor valor foi {menor_valor}")