''' Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para que o usuário tente descobrir qual foi
o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou não.'''

from random import randint
#metódo sleep faz ele "esperar"
from time import sleep
r1 = randint(0, 5)

print('::' * 20)
print('Estou pensando em um número entre 0 e 5.\nTente advinhar...')
print('::' * 20)

num = int(input('Qual é o seu palpite: '))

print('Analisando seu palpite...')
sleep(3)

if num == r1:
    print('Conseguiu me vencer! Acertou em cheio!')
else:
    print(f'Ganhei! Eu pensei no número {r1} e não no {num}!! Tente advinhar novamente')


