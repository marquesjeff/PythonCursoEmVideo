print("Analisador Completo")

total_idade = 0
mulheres_novas = 0
maior_idade = 0
nome_homem_mais_velho = ""

for c in range(1, 4+1):
    print(f"-----{c}ª Pessoa -----")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()

    total_idade += idade

    if sexo == "M":
        if idade > maior_idade:
            maior_idade = idade
            nome_homem_mais_velho = nome
    if sexo == "F" and idade < 20:
        mulheres_novas += 1



media_idade = total_idade / 4

print(f"A média de idade do grupo é de {media_idade:.1f}")
print(f"O homem mais velho é {nome_homem_mais_velho}, com {maior_idade} anos.")
print(f"Ao todo são {mulheres_novas} mulheres com menos de 20 anos.")
