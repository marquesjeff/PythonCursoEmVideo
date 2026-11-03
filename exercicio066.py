print("Vários números com flag")

num_valores = 0
soma = 0

while True:
    num = int(input("Digite um número [999] para parar: "))
    if num == 999:
        break
    num_valores += 1
    soma += num

print(f"A soma dos {num_valores} valores é {soma}")