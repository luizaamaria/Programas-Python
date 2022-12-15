#faça um programa que leia o comprimento do cateto ajacente de um triângulo
#retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot
c1 = float(input('Digite o comprimento do cateto oposto: '))
c2 = float(input('Digite o comprimento do cateto adjacente: '))
hipot = hypot(c1,c2)
print(f'A hipotenusa do triângulo é {hipot:0.2f}')


#sem utilizar os módulos
#c1 = float(input('Digite o comprimento do cateto oposto: '))
#c2 = float(input('Digite o comprimento do cateto adjacente: '))
#hipot = (c1 ** 2 + c2 ** 2) ** (1/2)
#print(f'A hipotenusa do triângulo é {hipot:0.2f}')
