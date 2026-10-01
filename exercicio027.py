print("Primeiro e último nome de uma pessoa")

nome = str(input("Digite seu nome completo: ")).strip().title()
primeiroNome = nome.split()[0]
# ultimoNome = nome.split()[-1]
ultimoEspaco = nome.rfind(" ") + 1
ultimoNome = nome[ultimoEspaco:]
print(f"Bem vindo(a) usuário(a), {nome}!")
print(f"Seu primeiro nome é {primeiroNome}.")
print(f"Seu último nome é {ultimoNome}.")
