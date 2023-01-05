'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
no final se ele foi aprovado(>7), foi pra recuperação(entre 5 e 6.9) ou se foi
reprovado direto(menos de 5).'''

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Parabéns! Você foi aprovado com média {:.1f}.'.format(media))
elif media >= 5 and media < 7:
    print('Você foi pra recuperação com média {:.1f}.'.format(media))
else:
    print('Sinto muito, você foi reprovado com média {:.1f}.'.format(media))


