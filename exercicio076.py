print("Lista de preços com uma Tupla")
chamada = "LISTA DE PREÇOS"
print("-"*48)
print(f"{chamada:^48}")
print("-"*48)

lista = ("Lápis", 1.75,
         "Borracha", 2.00,
         "Caderno", 15.00,
         "Estojo", 10.00,
         "Transferidor", 4.20,
         "Compasso", 9.99,
         "Mochila", 100.00,
         "Canetas", 22.50,
         "Livro", 35.00)

for pos, item in enumerate(lista):
    if pos % 2 == 0 or pos == 0:
        print(f"{item:.<35}", end=" ")
    else:
        print(f"R$ {item:>8.2f}")

print("-"*48)