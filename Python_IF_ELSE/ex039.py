'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
dele se alistar, ou se já passou do tempo de alistamento. Seu programa também deve
mostrar quanto tempo falta ou quanto tempo já passou do prazo.'''

ano_atual = 2022
nasc = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - nasc

if idade == 18:
    print('Você tem {} anos.'.format(idade))
    print('Está na hora de você se alistar ao serviço militar.')
elif idade < 18:
    print('Você ainda tem {} anos.'.format(idade))
    print('Ainda faltam {} anos para você se alistar.'.format(18 - idade))
else:
    print('Você já tem {} anos.'.format(idade))
    print('Já se passaram {} anos da época de se alistar.'.format(idade - 18))

