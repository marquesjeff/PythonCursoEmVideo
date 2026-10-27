print("Super Progressão Aritmética 3.0")

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

contagem = 1
proximo_termo = primeiro_termo
tem_numero = True
numero_termos = 10
contagem_termos = 0

while tem_numero:
    primeiro_da_rodada = True

    while contagem <= numero_termos:
        if not primeiro_da_rodada:
            print(" -> ", end="")

        print(proximo_termo, end="")
        primeiro_da_rodada = False

        proximo_termo += razao
        contagem += 1
        contagem_termos += 1

    print("\nPausa!")
    numero_termos = int(input("Quantos termos quer a mais?: "))

    contagem = 1

    if numero_termos == 0:
        tem_numero = False

print(f"Contagem finalizada com {contagem_termos} termos contabilizados.")
