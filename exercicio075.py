print("Analisando dados em uma Tupla")

numeros = ()

for c in range (0, 4):
    num = int(input(f"Digite o {c + 1}° número: "))
    numeros += (num, )

print(f"Você digitou os valores: {numeros}")
print(f"O valor 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O valor 3 apareceu na posição {numeros.index(3) + 1}°")
else:
    print("O valor 3 não apareceu na lista.")
print("Os valores pares digitados foram: ", end="")

for num in numeros:
    if num % 2 == 0:
        print(num,end=" ")



