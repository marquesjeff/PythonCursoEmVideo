print("Soma ímpares múltiplos de três")

num_multiplos = 0
soma_total = 0

for c in range(1, 500+1, 2):
    if c % 3 == 0:
        num_multiplos += 1
        soma_total += c

print(f"A soma dos {num_multiplos} valores solicitados é {soma_total}")

