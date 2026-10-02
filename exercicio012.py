print("Calculando descontos!")
produto = float(input("Qual o preço do produto? R$"))
desconto = produto * (5 / 100)
preco_final = produto - desconto
print(f"O produto que custava R${produto:.2f} após a promoção de 5% passará a custar R${preco_final:.2f}")

