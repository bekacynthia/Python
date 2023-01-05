'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
  para vencer.'''

from random import randint
computador = randint(0,10)
print('Sou seu computador. Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar?')
palpites = 0

acertou = False
while not acertou:
    pessoa = int(input('Coloque seu palpite: '))
    palpites += 1
    if pessoa > computador:
        print('Menos...tente outra vez!')
    elif computador > pessoa:
        print('Mais...tente outra vez!')
    elif computador == pessoa:
        acertou = True
        print('Parabéns! Você acertou!')
        print('Foram necessário(s) {} palpites pra você acertar.'.format(palpites))

