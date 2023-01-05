'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Digite um valor na tela: '))
n2 = int(input('Digite outro valor na tela: '))
choice = 0
while choice != 5:
    print('=-=' * 30)
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    print('-=-' * 30)
    choice = int(input('Digite sua escolha: '))
    if choice == 1:
        soma = n1 + n2
        print('A soma de {} e {} é igual a: {}.'.format(n1, n2, soma))
    elif choice == 2:
        mult = n1 * n2
        print('{} vezes {} é igual a {}.'.format(n1, n2, mult))
    elif choice == 3:
        if n1 > n2:
            print('{} é maior do que {}.'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior do que {}.'.format(n2, n1))
        else:
            print('{} é igual a {}.'.format(n1, n2))
    elif choice == 4:
        n1 = int(input('Digite um novo valor na tela: '))
        n2 = int(input('Digite mais um valor na tela: '))
    elif choice == 0 or choice > 5:
         print('Opção inválida! Tente novamente.')
if choice == 5:
    print('Sair do programa')



