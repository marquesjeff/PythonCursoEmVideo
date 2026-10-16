from datetime import datetime

print("Grupo da maioridade")

num_adultos = 0
num_criancas = 0
ano_atual = datetime.now().year

for c in range(1, 7+1):
    ano_nasc = int(input(f"Informe o ano de nascimento da {c}ª pessoa: "))
    if ano_atual - ano_nasc > 18:
        num_adultos += 1
    else:
        num_criancas += 1

print(f"Tivemos ao todo {num_adultos} adultos no grupo de idade.")
print(f"E {num_criancas} menores de idade.")