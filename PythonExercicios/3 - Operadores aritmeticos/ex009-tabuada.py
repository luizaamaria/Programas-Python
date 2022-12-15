#faça um programa  que leia um número  inteiro  qualquer e mostre a sua tabuada
n = int(input('Digite um número para ver a tabuada: '))

for count in range(10):
    print(f'{n} x {count + 1} = {n * (count + 1)}')
