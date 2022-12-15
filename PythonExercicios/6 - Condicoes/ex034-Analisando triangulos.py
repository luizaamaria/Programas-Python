'''
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''

med1 = float(input('Digite a 1° medida: '))
med2 = float(input('Digite a 2° medida: '))
med3 = float(input('Digite a 3° medida: '))

if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
    print('É um triângulo')
else:
    print('Não é um triângulo')
