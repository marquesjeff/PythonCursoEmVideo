print("Primeiro e último nome de uma pessoa")

nome = str(input("Digite seu nome completo: ")).strip().title()
primeiro_nome = nome.split()[0]
# ultimoNome = nome.split()[-1]
ultimo_espaco = nome.rfind(" ") + 1
ultimo_nome = nome[ultimo_espaco:]
print(f"Bem vindo(a) usuário(a), {nome}!")
print(f"Seu primeiro nome é {primeiro_nome}.")
print(f"Seu último nome é {ultimo_nome}.")
