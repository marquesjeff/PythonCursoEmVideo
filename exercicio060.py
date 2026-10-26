print("Calculando Fatorial!")

numero = int(input("Digite um número: "))
fatorial = 1
print(f"Calculando {numero}!")

while numero >= 1:
    fatorial *= numero
    if numero == 1:
        print(f"1 = ",end="")
    else:
        print(f"{numero} x ",end="")
    numero -= 1

print(fatorial)