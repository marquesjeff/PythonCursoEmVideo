
print("Maior e menor valores")

maior = 0
menor = 0
soma = 0
num_digitos = 0
tem_digito = True

while tem_digito:
    num = int(input("Digite um número: "))
    continuar = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]
    if continuar == "N":
        tem_digito = False

    if num_digitos == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    num_digitos += 1

media = soma / num_digitos
print(f"Você digitou {num_digitos} digitos e a média entre eles é {media:.2f}")
print(f"O maior número foi {maior} e o menor valor foi {menor}")
