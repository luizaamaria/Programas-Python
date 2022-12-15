#escreva um programa que converta uma temperatura digitada em °C para °F

c = float(input('Informe a temperatura em °C: '))
#não precisa de parenteses nesse ex, pois a ordem de procedencia da expressão é exatamente a ordem que os operadores aparecem
f = 9*c/5+32
print(f'A temperatura de {c}°C corresponde a {f}°F')
