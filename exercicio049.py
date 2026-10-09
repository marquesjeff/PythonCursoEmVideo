print("Tabuada 2.0")

numero = int(input("Digite um número para ver sua tabuada: "))

for count in range(0, 10+1):
    print(f"{count} x {numero} = {count * numero}")