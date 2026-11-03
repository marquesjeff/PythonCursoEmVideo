print("Análise de dados do grupo")

num_adultos = 0
num_homens = 0
jovens = 0
sexo = ""

while True:
    print("-" * 20)
    print("Cadastre uma pessoa!")
    print("-" * 20)
    idade = int(input("Idade: "))
    if idade > 18:
        num_adultos += 1

    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while sexo not in ("M", "F"):
        print("Opção inválida! Tente novamente!")
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

    if sexo == "M":
        num_homens += 1
    if sexo == "F" and idade < 20:
        jovens += 1
    continuar = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]


    if continuar == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {num_adultos}")
print(f"Total de homens cadastrados: {num_homens}")
print(f"Número de mulheres com menos de 20 anos: {jovens}")