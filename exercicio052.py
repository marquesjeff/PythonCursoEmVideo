print("Números primos")

numero = int(input("Digite um número: "))
num_vezes_divisivel = 0


for c in range(1, numero + 1):
    if numero % c == 0:
        print(f"\033[7:32:40m {c} \033[m", end=" ")
        num_vezes_divisivel += 1
    else:
        print(f"\033[0:32:40m {c} \033[m", end=" ")

print(f"\nO número {numero} foi divisível {num_vezes_divisivel} vezes.")

if num_vezes_divisivel == 2:
    print("E por isso ele É um número primo.")
else:
    print("E por isso ele NÃO É um número primo.")
