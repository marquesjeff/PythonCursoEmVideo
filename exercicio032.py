from datetime import datetime

print("Ano Bissexto!")
ano = int(input("Informe o ano que deseja analisar [0 para Ano Atual]: "))
ano_atual = datetime.now().year

if ano == 0:
    ano = ano_atual

if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print(f"O ano {ano} é um ano bissexto!")
else:
    print(f"O ano {ano} não é um ano bissexto!")

print(ano_atual)