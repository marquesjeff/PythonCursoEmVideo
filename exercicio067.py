print("Tabuada 3.0")

while True:
    num = int(input("Informe o número: "))
    if num < 0:
        print("Programa encerrado!")
        break
    else:
        for c in range(0, 10+1):
            print(f"{num} x {c} = {num * c}")
    print("-" * 20)