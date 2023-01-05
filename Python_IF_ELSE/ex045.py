'''Crie um programa pra jogar pedra, papel e tesoura com o computador.'''

from random import randint
from time import sleep
eu = str(input('PEDRA, PAPEL, TESOURA?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
comp = randint(1,3)
if comp == 1:
    print('PEDRA')
elif comp == 2:
    print('PAPEL')
else:
    print('TESOURA')

if eu == 'pedra' and comp == 1:
    print('Deu empate!')
elif eu == 'papel' and comp == 1:
    print('Você venceu!')
elif eu == 'tesoura' and comp == 1:
    print('A-ha! Eu ganhei de você!')
elif eu == 'pedra' and comp == 2:
    print('A-ha! Eu ganhei de você!')
elif eu == 'papel' and comp == 2:
    print('Deu empate!')
elif eu == 'tesoura' and comp == 2:
    print('Parabéns! Você me venceu!')
elif eu == 'pedra' and comp == 3:
    print('Parabéns! Você me venceu!')
elif eu == 'papel' and comp == 3:
    print('A-ha! Eu ganhei de você!')
elif eu == 'tesoura' and comp == 3:
    print('Deu empate!')




