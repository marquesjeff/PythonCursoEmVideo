print("Maior e Menor da Sequência")

menor_peso = 0
maior_peso = 0

for c in range(1, 5+1):
    peso = float(input(f"Peso da {c}ª pessoa: "))
    if c == 1:
        menor_peso = peso
        maior_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso
        if peso > maior_peso:
            maior_peso = peso

print(f"O maior peso lido foi de {maior_peso:.1f}kg")
print(f"O menor peso lido foi de {menor_peso:.1f}kg")