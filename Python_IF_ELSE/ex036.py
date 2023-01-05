'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite em quantos anos ele vai pagar: '))

prestacao = casa / (anos * 12)
print('A prestação mensal ficou no valor de: R${:.2f}.'.format(prestacao))
print('E 30% do seu salário equivale a: R${:.2f}.'.format(salario * 30 / 100))
if prestacao > salario * 30 / 100:
    print('Sinto muito, seu empréstimo foi negado.')
else:
    print('PARABÉNS! Seu empréstimo foi aprovado.')
