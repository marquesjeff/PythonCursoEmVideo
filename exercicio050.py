print("Soma dos pares!")

soma = 0
cont_pares = 0

for c in range(1, 6 + 1):
    numero = int(input(f"Número #{c}: "))
    if numero % 2 == 0:
        soma += numero
        cont_pares += 1

if soma > 0:
    print(f"Foram digitados {cont_pares} números pares e a soma entre eles é {soma}")
else:
    print("Você informou apenas números ímpares!")