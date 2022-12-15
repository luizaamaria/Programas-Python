#faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "A"
#em que posição ela aparece na primeira e na ultima vez

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")} vezes')
print(f'A letra A aparece pela primeira vez na posição {frase.find("A")+1}')
print(f'A letra A aparece pela ultima vez na posição {frase.rfind("A")+1}')

