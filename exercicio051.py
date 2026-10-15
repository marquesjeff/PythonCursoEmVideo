print("Progressão Aritmética")

print("10 termos de uma PA!")

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo_termo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo_termo + razao, razao):
    print(c, end=" -> ")

print("Acabou")