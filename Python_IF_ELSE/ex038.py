''' Escreva um programa que leia dois números inteiros e compare-os. Mostre qual deles
é o maior, o menor ou se ambos são iguais.'''

num1 = int(input('Digite o 1° número inteiro: '))
num2 = int(input('Digite o 2° número inteiro: '))

if num1 > num2:
    print('O primeiro número é maior do que o segundo.')
elif num2 > num1:
    print('O segundo número é maior do que o primeiro.')
else:
    print('Ambos os números são iguais.')
