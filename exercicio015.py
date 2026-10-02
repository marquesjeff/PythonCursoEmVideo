print("Aluguel de carros!")
dias_alugados = int(input("Quantos dias alugado?: "))
km_rodados = float(input("Quantos km rodados?: "))
aluguel_dia = 60
preco_km = 0.15
total_pagar = (dias_alugados * aluguel_dia) + (km_rodados * preco_km)
print(f"O total a pagar é de R${total_pagar:.2f}")
