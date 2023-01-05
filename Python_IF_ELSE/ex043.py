'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura(m/cm): '))
IMC = peso / (altura * altura)

if IMC < 18.5:
    print('IMC: {:.2f}. Você está abaixo do peso.'.format(IMC))
elif IMC >= 18.5 and IMC < 25:
    print('IMC: {:.2f}. Você está no peso ideal.'.format(IMC))
elif IMC >= 25 and IMC < 30:
    print('IMC: {:.2f}. Você está de sobrepeso.'.format(IMC))
elif IMC >= 30 and IMC < 40:
    print('IMC: {:.2f}. Você está obeso(a).'.format(IMC))
else:
    print('IMC: {}. Você está com obesidade mórbida.'.format(IMC))
