print("Calculando descontos!")
produto = float(input("Qual o preço do produto? R$"))
desconto = produto * (5 / 100)
precoFinal = produto - desconto
print(f"O produto que custava R${produto:.2f} após a promoção de 5% passará a custar R${precoFinal:.2f}")

