print("Conversor de Base Numérica!")

numero = int(input("Digite um número inteiro: "))
base_conversao = int(input("Escolha a base para conversão: \n[1] Binário "
                           "\n[2] Octal"
                           "\n[3] Hexadecimal "
                           "Sua Opção: "))

if base_conversao == 1:
    binario = bin(numero)[2:]
    print(f"{numero} em binário é {binario}")
elif base_conversao == 2:
    octal = oct(numero)[2:]
    print(f"{numero} em Octal é {octal}")
elif base_conversao == 3:
    hexadecimal = hex(numero)[2:]
    print(f"{numero} em Hexadecimal é {hexadecimal}")
else:
    print("Opção Inválida! Tente novamente.")