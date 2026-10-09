print("Contagem de pares!")

num_pares = 0

for c in range(1, 50+1):
    if c % 2 == 0:
        print(c, end=" ")
        num_pares += 1

print(f"\nEntre 1 e 50 existem {num_pares} números pares")