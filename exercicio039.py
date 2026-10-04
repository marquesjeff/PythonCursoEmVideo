from datetime import datetime

print("Alistamento militar!")

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade < 18:
    print(f"Você tem {idade} anos, portanto ainda faltam {18 - idade} anos para o alistamento!")
elif idade == 18:
    print(f"Você tem {idade} anos!É hora de se alistar!")
elif idade > 18:
    saldo = idade - 18
    print(f"Você tem mais de 18 anos! Você deveria ter se alistado há {saldo} anos atrás!")