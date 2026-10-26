print("Progressão Aritmética 2.0")

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
contagem = 1

print(primeiro_termo, end="")
proximo_termo = primeiro_termo + razao

while contagem < 10:
    print(f" -> {proximo_termo}", end="")
    proximo_termo += razao
    contagem += 1
