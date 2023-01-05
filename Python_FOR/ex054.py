'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas já são maiores.'''

maior = 0
menor = 0
from datetime import date
atual = date.today().year
for c in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos.'.format(idade))
    if idade >= 18:
        maior += 1
        print('Essa pessoa é de maior.')
    else:
        menor += 1
        print('Essa pessoa é de menor.')
print('{} pessoas são maiores de idade,'.format(maior))
print('E {} pessoas são menores de idade.'.format(menor))






