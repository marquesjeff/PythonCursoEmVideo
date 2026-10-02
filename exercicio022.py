print("Analisando Texto!")

nome = str(input("Digite seu nome completo: "))
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
letras_nome = len(nome.replace(" ", "").strip())
primeiro_nome = nome.split()[0]
letras_primeiro_nome = len(primeiro_nome)


print("Analisando seu nome...")
print(f"Seu nome em maiuscúlas é {nome_maiusculo}")
print(f"Seu nome em minúsculo é {nome_minusculo}")
print(f"Seu nome completo tem {letras_nome} letras")
print(f"Seu primeiro nome é {primeiro_nome} e ele tem {letras_primeiro_nome} letras")