print("Sequência de Fibonacci v1.0")

numero_termos = int(input("Quantos termos você quer mostrar?: "))
termo1 = 0
termo2 = 1
proximo = termo1 + termo2

print(f"{termo1} -> {termo2} -> ",end="")

while (numero_termos - 2 ) > 0:
    proximo = termo1 + termo2
    print(f"{proximo} -> ",end="")
    termo1 = termo2
    termo2 = proximo
    numero_termos -= 1
print("Fim.")