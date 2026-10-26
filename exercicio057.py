print("Validação de Dados")

sexo_verdadeiro = False
while not sexo_verdadeiro:
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
    if sexo == "M" or sexo == "F":
        print(f"Sexo {sexo} registrado com sucesso!")
        sexo_verdadeiro = True
    else:
        print("Dados Inválidos! Tente novamente.")

