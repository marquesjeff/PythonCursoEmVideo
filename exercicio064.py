print("Tratando vários valores v1.0")

num_digitos = 0
soma = 0
tem_digito = True

while tem_digito:
    num = int(input("Digite um número [999] para parar: "))
    if num == 999:
        tem_digito = False
    else:
        soma += num
        num_digitos += 1

print(f"Você digitou {num_digitos} digitos e a soma entre ele é {soma}")
