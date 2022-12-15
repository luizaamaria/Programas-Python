'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando $0,50 por km para viagem de até 200km e
$0,45 para viagens mais longas.
'''
distancia = float(input('Qual a distância da sua viagem: '))

acima  = distancia * 0.45
abaixo = distancia * 0.50
if distancia <= 200:
    print(f'O preço da sua passagem será de R$:{abaixo}')
else:
    print(f'O preço da sua passagem será de R$:{acima}')

#/////////////////////////////////////////////////////////


distancia = float(input('Qual a distância da sua viagem: '))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f'O preço da sua passagem será de R$:{preco}')
