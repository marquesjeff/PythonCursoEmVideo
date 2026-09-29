import random

print("Mudando a ordem numa lista")
aluno1 = str(input("Primeiro Aluno: ")).strip().capitalize()
aluno2 = str(input("Segundo Aluno: ")).strip().capitalize()
aluno3 = str(input("Terceiro Aluno: ")).strip().capitalize()
aluno4 = str(input("Quarto Aluno: ")).strip().capitalize()
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(listaAlunos)
print(f"A lista final será {listaAlunos}")
