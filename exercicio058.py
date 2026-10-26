from time import sleep
from random import randint

num_pc = randint(0, 10)
print("Jogo do Adivinha 2.0")
sleep(1)
print("Tente adivinhar um número de 0 a 10")
sleep(1)
palpite_certo = False
num_tentativas = 0
while not palpite_certo:
    num_player = int(input("Seu palpite: "))
    if num_player == num_pc:
        num_tentativas += 1
        print("Você VENCEU!")
        sleep(1)
        print(f"O número correto era {num_pc}!")
        print(f"Você venceu com {num_tentativas} tentativas!")
        palpite_certo = True
    elif num_player < num_pc:
        num_tentativas += 1
        print("Mais... Tente novamente!")
    elif num_player > num_pc:
        num_tentativas += 1
        print("Menos... Tente novamente!")