#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#dollar em real: 5,18

real = float(input('Qual valor você possui em real? R$'))
dolar = real / 5.18
print(f'Com R${real :.2f} você pode comprar U${dolar :.2f}')
