print("Lendo o nome de uma cidade!")

cidade = str(input("Informe a cidade em que você nasceu: ")).strip().upper()
santo_cidade = cidade[:5] == "SANTO"
print(f"Cidade começa com a palavra 'Santo'? {santo_cidade}")