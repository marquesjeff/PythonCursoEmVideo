import random

print("Aleatoriamente selecionando um item numa lista.")
aluno1 = str(input("Primeiro Aluno: ")).strip()
aluno2 = str(input("Segundo Aluno: ")).strip()
aluno3 = str(input("Terceiro Aluno: ")).strip()
aluno4 = str(input("Quarto Aluno: ")).strip()
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_escolhido = random.choice(lista_alunos)
print(f"O aluno escolhido foi {aluno_escolhido}")
