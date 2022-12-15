'''
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Informe o valor do seu salário: '))
superior = salario + (salario * 10 / 100)
inferior = salario + (salario * 15 / 100)

if salario <= 1250.00:
    print(f'O valor do seu salário atual é de: {inferior}')
else:
    print(f'O valor do seu salário atual é de: {superior}')

