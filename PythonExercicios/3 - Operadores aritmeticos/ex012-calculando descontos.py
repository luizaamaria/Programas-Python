#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Qual o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print(f'O produto que custava {preco:.2f}, na promoção com desconto de 5% vai custar {novo:.2f}')
