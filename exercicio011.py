print("Pintando uma parede!")
larg = float(input("Qual a largura da parede? Em metros: "))
alt = float(input("Qual a altura da parede? Em metros: "))
area = larg * alt
quantidade = area / 2
print(f"A dimensão da parede é {larg}x{alt} e sua área é de {area}m²")
print(f"Para pintar essa parede serão necessários {quantidade}l de tinta.")
