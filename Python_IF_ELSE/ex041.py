'''A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SENIOR
- Acima de 25 anos: MASTER'''

nasc = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = 2022
idade = ano_atual - nasc

if idade <= 9:
    print('{} anos. Atleta MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('{} anos. Atleta INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('{} anos. Atleta JUNIOR.'.format(idade))
elif idade > 19 and idade <= 25:
    print('{} anos. Atleta SENIOR.'.format(idade))
else:
    print('{} anos. Atleta MASTER.'.format(idade))
