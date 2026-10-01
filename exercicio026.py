print("Primeira e última ocorrência de uma String!")

frase = str(input("Digite uma frase: ")).strip().upper()
vezesA = frase.count("A")
primeiroA = frase.find("A") + 1
ultimoA = frase.rfind("A") + 1
print(f"A letra A aparece na frase {vezesA} vezes")
print(f"O primeiro A aparece na posição {primeiroA}")
print(f"E o último A aparece na posição {ultimoA}")
