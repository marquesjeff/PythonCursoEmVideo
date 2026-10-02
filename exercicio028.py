import random
from time import sleep

print("Jogo do adivinha 1.0")
print("Vou pensar em um número de 0 a 5. Tente adivinhar...")

num_usuario = int(input("Em que número eu pensei: "))
numero_maquina = random.randint(0, 6)

print("Processando...")
sleep(2)

if numero_maquina == num_usuario:
    print(f"VOCÊ ACERTOU! Juntos pensamos no número {numero_maquina}!")
else:
    print(f"VOCÊ ERROU! Eu pensei no número {numero_maquina} e não no {num_usuario}!")