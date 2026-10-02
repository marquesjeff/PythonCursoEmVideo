print("Primeira e última ocorrência de uma String!")

frase = str(input("Digite uma frase: ")).strip().upper()
vezes_a = frase.count("A")
primeiro_a = frase.find("A") + 1
ultimo_a = frase.rfind("A") + 1
print(f"A letra A aparece na frase {vezes_a} vezes")
print(f"O primeiro A aparece na posição {primeiro_a}")
print(f"E o último A aparece na posição {ultimo_a}")
