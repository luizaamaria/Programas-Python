#Faça um programa que leia três números e mostre qual é o menor e qual é o maior.

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))

if n1 > n2 and n1 > n3:
    print(f'Maior: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'Maior: {n2}')
else:
    print(f'Maior: {n3}')

if n1 < n2 and n1 < n3:
    print(f'Menor: {n1}')
elif n2 < n1 and n2 < n3:
    print(f'Menor {n2}')
else:
    print(f'Menor {n3}')

if n1 == n2 and n2 == n3:
    print('Os números são iguais!')

#/////////////////////////////////////
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    menor = n2
if n3 > n1 and n3 > n2:
    menor = n3

print(f'Maior: {menor}')
print(f'Menor: {maior}')

