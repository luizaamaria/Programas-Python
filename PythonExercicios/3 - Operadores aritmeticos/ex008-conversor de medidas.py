#escreva um programa que leia um valor em metros e a exiba convertido  em centimetros e milimetros

medida = float(input('Uma distancia em metros: '))
dc = medida *10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print(f'A media de {medida}m corresponde a {cm}cm e {mm}mm'
      f' e {dc}decim e {dam}decam e {hm}hec e {km}km')
