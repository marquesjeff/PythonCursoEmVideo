print("Analisando Texto!")

nome = str(input("Digite seu nome completo: "))
nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
letrasNome = len(nome.replace(" ", "").strip())
primeiroNome = nome.split()[0]
letrasPrimeiroNome = len(primeiroNome)


print("Analisando seu nome...")
print(f"Seu nome em maiuscúlas é {nomeMaiusculo}")
print(f"Seu nome em minúsculo é {nomeMinusculo}")
print(f"Seu nome completo tem {letrasNome} letras")
print(f"Seu primeiro nome é {primeiroNome} e ele tem {letrasPrimeiroNome} letras")