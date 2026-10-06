print("Analisando triângulos 2.0")

segmento1 = float(input("Primeiro segmento: "))
segmento2 = float(input("Segundo segmento: "))
segmento3 = float(input("Terceiro segmento: "))

if segmento1 + segmento2 > segmento3 and segmento1 + segmento3 > segmento2 and segmento2 + segmento3 > segmento1:
    print("Os segmentos acima PODEM formar um triângulo!")
    if segmento1 == segmento2 == segmento3:
        print("O triângulo será do tipo EQUILÁTERO!")
    elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
        print("O triângulo será do tipo ISÓSCELES!")
    elif segmento1 != segmento2 != segmento3:
        print("O triângulo será do tipo ESCALENO!")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo!")