print(" Estatísticas em produtos")


print("-"*20)
print("Lojas On-Line")
print("-"*20)

total_compra = 0
mais_mil = 0
menor_preco = 0
nome_menor = ""
continuar = ""

while True:
    nome_produto = str(input("Nome do produto: ")).strip()
    preco = float(input("Preço R$"))
    total_compra += preco
    if preco > 1000:
        mais_mil += 1

    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        nome_menor = nome_produto

    continuar = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    while continuar not in("S", "N"):
        print("Opção Inválida! Tente novamente!")
        continuar = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    if continuar == "N":
        break

print(f"O total da compra foi R${total_compra:.2f}")
print(f"Total de produtos que custam mais de R$1000.00: {mais_mil}")
print(f"O produto mais barato foi {nome_menor} com um preço de R${menor_preco:.2f}")