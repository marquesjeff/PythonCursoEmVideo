print("Procurando por uma String dentro de outra!")

nome = str(input("Digite seu nome completo: ")).strip().upper()
silva_nome = "SILVA" in nome

print(f"Seu nome tem 'Silva'? {silva_nome}")
