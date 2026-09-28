print("Aluguel de carros!")
diasAlugados = int(input("Quantos dias alugado?: "))
kmRodados = float(input("Quantos km rodados?: "))
aluguelDia = 60
precoKm = 0.15
totalPagar = (diasAlugados * aluguelDia) + (kmRodados * precoKm)
print(f"O total a pagar é de R${totalPagar:.2f}")
