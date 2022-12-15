#Crie um programa que leia o nome de uma pessoa e mostre:
#O nome com todas as letras minusculas.
#Quantas letras tem no total (sem considerar os espaços)
#Quantas letras tem o primeiro nome

nome = input('Qual é o seu nome? ').strip()
print(f'Seu nome em minusculo é {nome.lower()}')
print(f'Seu nome contém: {len(nome) - nome.count(" ")} letras')
#print(f'Seu primeiro nome tem no total {nome.find(" ")} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]}, e ele tem {len(separa[0])} letras')




