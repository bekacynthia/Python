'''Faça um programa que leia um número inteiro e diga se ele é ou não
 um número primo.'''

num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        tot = tot + 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if tot == 2:
    print('\nO número {} é primo'.format(num))
else:
    print('\nO número {} não é primo'.format(num))




