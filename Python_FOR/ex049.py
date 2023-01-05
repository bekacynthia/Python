'''Refaça o desafio 9 da tabuada, s[o que agora deixando o suário escolher o número
e utilizando o laço for.'''

tab = 0
c = 1
num = int(input('escolha um número: '))
for c in range(1, 11):
    tab = num * c
    print('{} X {} = {}'.format(num, c, tab))