#faça um algoritmo que leia o salario de um funcionário e mostre seu novo salario, com 15% de aumento

salario = float(input('Qual o valor do salario do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print(f'O novo salario com aumento de 15% é de {novo:.2f}')
