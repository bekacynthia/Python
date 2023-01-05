'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o
 seu preço normal e condição de pagamento:

 – à vista dinheiro/cheque: 10% de desconto
 – à vista no cartão: 5% de desconto
 – em até 2x no cartão: preço formal
 – 3x ou mais no cartão: 20% de juros'''

print('{:=^100}'.format('LOJAS BEKABU'))
preco = float(input('Digite o preço do produto: R$'))
print('-=-' * 30)
print("""FORMAS DE PAGAMENTO:
   1 – à vista dinheiro/cheque: 10% de desconto
   2 – à vista no cartão: 5% de desconto
   3 – em até 2x no cartão: preço formal
   4 – 3x ou mais no cartão: 20% de juros""")
print('-=-' * 30)
opcao = int(input('Escolha a opção de pagamento: '))
if opcao == 1:
    preco = preco - (preco * 10 / 100)
    print('O valor final da compra foi R${} com desconto de 10%.'.format(preco))
elif opcao == 2:
    preco = preco - (preco * 5 / 100)
    print('O valor finaç da compra foi R${} com 5% de desconto.'.format(preco))
elif opcao == 3:
    parcela = int(input('Em 1 ou 2x?'))
    if parcela == 1:
        preco = preco * 1
        print('O valor da compra foi de R${}.'.format(preco))
    elif parcela == 2:
        preco = preco / 2
        print('O valor parcelado em duas vezes foi de R${}.'.format(preco))
    else:
        print('Opção inválida')
elif opcao == 4:
    parcela = int(input('Em quantas vezes você quer parcelar? '))
    preco = (preco + preco * 20 / 100) / parcela
    print('O valor parcelado em três vezes com juros foi de R${}.'.format(preco))
else:
    print('Opção inválida! Tente novamente!')



