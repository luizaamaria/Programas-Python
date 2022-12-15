#o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
al1 = input('Informe o nome do 1° aluno: ')
al2 = input('Informe o nome do 2° aluno: ')
al3 = input('Informe o nome do 3° aluno: ')
al4 = input('Informe o nome do 4° aluno: ')

alunos = [al1, al2, al3, al4]
shuffle(alunos)

print(f'A ordem de apresentação dos trabalhos será: {alunos}')
