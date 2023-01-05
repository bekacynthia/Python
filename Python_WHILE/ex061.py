'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
 usando a estrutura while.'''

print('GERADOR DE PA')
print('=-=' * 20)
primeiro = int(input('Digite o primeiro termo de uma progressão aritmética: '))
razao = int(input('Digite a razão: '))
print('=-=' * 20)
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')



