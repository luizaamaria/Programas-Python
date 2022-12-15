#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
#Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
#Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)

from datetime import date
ano = int(input('Digite o ano que quer analisar? \n Ou digite 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Bissexto')
else:
    print('Não é bissexto')