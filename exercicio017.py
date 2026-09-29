import math

print("Catetos e Hipotenusa")
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")