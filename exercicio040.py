print("Média Clássica!")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2

print(f"A média do aluno foi de {media:.1f}")
if media < 5.0:
    print("REPROVADO!")
elif 5.0 <= media <= 6.9:
    print("RECUPERAÇÃO!")
else:
    print("APROVADO!")
