print("Procurando por uma String dentro de outra!")

nome = str(input("Digite seu nome completo: ")).strip().upper()
silvaNome = "SILVA" in nome

print(f"Seu nome tem 'Silva'? {silvaNome}")
