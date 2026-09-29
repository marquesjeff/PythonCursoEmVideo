import random

print("Aleatoriamente selecionando um item numa lista.")
aluno1 = str(input("Primeiro Aluno: ")).strip()
aluno2 = str(input("Segundo Aluno: ")).strip()
aluno3 = str(input("Terceiro Aluno: ")).strip()
aluno4 = str(input("Quarto Aluno: ")).strip()
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
alunoEscolhido = random.choice(listaAlunos)
print(f"O aluno escolhido foi {alunoEscolhido}")
