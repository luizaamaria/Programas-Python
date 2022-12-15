#faça um programa que leia  um ângulo qualquer e mostre na tela
#o valor do seno cosseno e tangente desse ângulo

from math import cos, sin, tan, radians
angulo = float(input('Informe um ângulo qualquer: '))
#convertendo para radianos
s = sin(radians(angulo))
c = cos(radians(angulo))
t = tan(radians(angulo))

print(f'O seno de {angulo} é {s:.2f}, cosseno é {c:.2f} e seu tangente é {t:.2f}')



