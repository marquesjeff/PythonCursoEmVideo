from random import randint
from time import sleep

print("Game! Pedra, Papel, Tesoura!")

jogador = int(input("[0] Pedra \n[1] Papel \n[2]Tesoura\nQual sua jogada?: "))
pc = randint(0, 2)

if  0 <= jogador <= 2:
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")
    sleep(1)

    if pc == 0:
        print("Computador jogou PEDRA!")
    elif pc == 1:
        print("Computador jogou PAPEL!")
    elif pc == 2:
        print("Computador jogou TESOURA!")

    if jogador == 0:
        print("Jogador jogou PEDRA!")
    elif jogador == 1:
        print("Jogador jogou PAPEL!")
    elif jogador == 2:
        print("Jogador jogou TESOURA!")

    if (pc == 0 and jogador == 2) or (pc == 1 and jogador == 0) or (pc == 2 and jogador == 1):
        print("Computador VENCE!")
    elif (jogador == 0 and pc == 2) or (jogador == 1 and pc == 0) or (jogador == 2 and pc == 1):
        print("Jogador VENCE!")
    else:
        print("EMPATE!")
else:
    print("Opção INVÁLIDA! Execute o programa novamente!")



