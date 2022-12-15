#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira:
#ex: digite um número: 6.127 | o número 6.127 tem a parte inteira 6

from math import trunc
real = float(input('Digite um número: '))
num = trunc(real)
print(f'O número {real} tem a parte inteira {num}')

#sem importar os módulos
#real = float(input('Digite um número: '))
#print(f'O número {real} tem a parte inteira {int(real)}')
