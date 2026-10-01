import random
from time import sleep

print("Jogo do adivinha 1.0")
print("Vou pensar em um número de 0 a 5. Tente adivinhar...")

numUsuario = int(input("Em que número eu pensei: "))
numeroMaquina = random.randint(0, 6)

print("Processando...")
sleep(2)

if numeroMaquina == numUsuario:
    print(f"VOCÊ ACERTOU! Juntos pensamos no número {numeroMaquina}!")
else:
    print(f"VOCÊ ERROU! Eu pensei no número {numeroMaquina} e não no {numUsuario}!")