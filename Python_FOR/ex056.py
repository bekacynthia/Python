'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem
mais velho e quantas mulheres têm menos de 20 anos.'''

somaidade = 0
idadehomemvelho = 0
nomehomemvelho = ''
quantmulheres = 0

for p in range(1, 5):
    print('-----------{}° Pessoa: ---------'.format(p))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo[M/F]: '))
    somaidade += idade
    media = somaidade / 4
    if p == 1 and sexo == 'M':
        idadehomemvelho = idade
        nomehomemvelho = nome
    if idade > idadehomemvelho and sexo == 'M':
        idadehomemvelho = idade
        nomehomemvelho = nome
    if sexo == 'F' and idade < 20:
        quantmulheres += 1
print('A média da idade do grupo é: {}.'.format(media))
print('O nome do homem mais velho é: {}.'.format(nomehomemvelho))
print('A quantidade de mulheres com menos de vinte anos é: {}.'.format(quantmulheres))








