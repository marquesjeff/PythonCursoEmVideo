print("Limite de Velocidade!")

velocidade = float(input("Informe a velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado por ultrapassar o limite de 80km/h!")
    print(f"O preço da multa será de R${multa:.2f}")
else:
    print("Você está no limite de velocidade.")

print("Dirija com segurança.")
