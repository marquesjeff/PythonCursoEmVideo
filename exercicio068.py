from time import sleep
from random import randint

print("Jogo do Par ou Ímpar")

num_vitorias = 0

while True:
    jogada_pc = randint(0, 10)
    jogada_player1 = int(input("Seu valor: "))
    escolha = str(input("Par ou Ímpar [P/I]: ")).upper().strip()[0]
    if escolha not in ("P", "I"):
        print("Opção inválida! Tente novamente!")
        continue
    soma_jogada = jogada_pc + jogada_player1
    sleep(1)

    print("-" * 30)
    resultado = "P" if soma_jogada % 2 == 0 else "I"
    print(f"Você jogou {jogada_player1} e o computador jogou {jogada_pc}!")
    print(f"Total de {soma_jogada}. ", end="")
    print("Valor par!" if resultado == "P" else "Valor ímpar!")
    print("-" * 30)
    sleep(1)

    if escolha == resultado:
        print("\033[0:32:40m Você venceu! \033[m")
        num_vitorias += 1
        sleep(0.5)
        print("Vamos jogar novamente!")
        sleep(0.5)
    else:
        print("Você perdeu!")
        break


sleep(0.5)

print(f"\033[0:31:40m GAME OVER \033[m")
print(f"Você venceu um total de {num_vitorias} vezes.")