'''Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando so espaços.'''

frase = str(input('Por favor, digite uma frase sem acentos: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if junto == inverso:
    print('{} É UM PALÍNDROMO!'.format(frase))
else:
    print('{} não é um palíndromo.'.format(frase))

'''Sem o for(forma mais simples e enxuta de executar):

frase = str(input('Por favor, digite uma frase sem acentos: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print('{} É UM PALÍNDROMO!'.format(frase))
else:
    print('{} não é um palíndromo.'.format(frase))'''

