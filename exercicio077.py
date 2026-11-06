print("Contando vogais em Tuplas")

lista = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO",
         "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR",
         "MERCADO", "PROGRAMADOR", "FUTURO")

for palavra in lista:
    print(f"Na palavra {palavra} temos: ", end="")
    for letra in palavra:
        if letra in ("A", "E", "I", "O", "U"):
            print(letra, end=" ")
    print()