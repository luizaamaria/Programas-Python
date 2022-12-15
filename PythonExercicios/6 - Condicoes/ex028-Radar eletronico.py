'''Escreva um programa que leia a velocidade de um carro:
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar $7,00 por cada Km acima do limite'''

vel = float(input('Qual a velocidade do seu carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'Velocidade acima do limite\nMulta no valor de: {multa}')
else:
    print('Velocidade dentro do limite!')


