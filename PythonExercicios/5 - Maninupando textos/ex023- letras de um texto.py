#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Qual o nome da cidade ? ').strip()
print(cidade[:5].upper() == 'SANTO')

