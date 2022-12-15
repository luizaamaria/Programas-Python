#um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele , lendo o nome deles e escrevendo o nome dos escolhidos

from random import choice

al1 = str(input('Informe o nome do 1° aluno: '))
al2 = str(input('Informe o nome do 2° aluno: '))
al3 = str(input('Informe o nome do 3° aluno: '))
al4 = str(input('Informe o nome do 4° aluno: '))

alunos = [al1, al2, al3, al4]
sorteado = choice(alunos)

print(f'O aluno sorteado foi o {sorteado}')
