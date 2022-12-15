#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultiimo nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()
#a função split vai fatiar esse nome inteiro, ou seja dividir ele em pedaços
separa = nome.split()
print(f'Seu primeiro nome é: {separa[0]}')
print(f'Seu ultimo nome é:   {separa[-1]}')

