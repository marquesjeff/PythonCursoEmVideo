print("Custo de Viagem")

distancia = float(input("Informe a distância da viagem em km: "))
preco = 0
custoViagem = 0

if distancia > 200:
    preco = 0.45
    custoViagem = preco * distancia
else:
    preco = 0.50
    custoViagem = preco * distancia

print(f"A viagem terá uma distância de {distancia:.1f}")
print(f"O preço da passagem será de R${custoViagem:.2f}")
