#faça um programa que leia a largura e a altura de uma parede em metros , calcule a sua
#área e a quantidade  de tinta necessária  para pintá-la ,sabendo  que cada litro de tinta, pinta uma parea de 2m

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'sua parade tem a dimensão de {larg} x {alt} e sua área é de {area}m')
tinta = area / 2
print(f'Para pintar sua parede, é necessário de {tinta}l de tinta')
