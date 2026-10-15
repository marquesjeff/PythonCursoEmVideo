print("Detector de Palíndromo")

frase = str(input("Digite uma frase: "))
frase_mod = frase.strip().upper().replace(" ", "")

frase_inversa = ""
for c in range(len(frase_mod) -1, -1, -1):
    frase_inversa += frase_mod[c]


print(f"O inverso de {frase_mod} é {frase_inversa}")

if frase_mod == frase_inversa:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")