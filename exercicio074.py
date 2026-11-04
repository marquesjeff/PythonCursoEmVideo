from random import randint

print("Maior e menor valor em uma Tupla")

numeros = ()

for c in range(5):
    num = randint(0, 9)
    numeros += (num, )

print(f"Os números sorteados foram: {numeros}")
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")