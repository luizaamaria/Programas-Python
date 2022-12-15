#Crie um programa que leia um número e mostre na tela se ele é par ou impar

num = int(input('Digite um numero: '))
if num % 2 == 0:
    print(f'O numéro {num} é par')
else:
    print(f'O número {num} é impar')