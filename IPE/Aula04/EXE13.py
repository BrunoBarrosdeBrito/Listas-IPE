'''
13)	Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
'''
kwh = float(input('Digite a quantidade de energia consumida em Kwh(kilowatt-hora): '))
print('-'*80)
print('Quando for digitar qual foi o lugar que foi consumido a energia, digite um desses três:')
print('- Residencial \n- Comercial \n- Industrial')
print('Dependendo a sua escolha, vai ter valores diferentes para cada tipo.')
print('-'*80)
tipo = str(input('Digite o local onde teve o consumo de energia: '))
if tipo == 'Residencial':
    if kwh <= 500:
        print('O valor a ser pago é {:.2f} reais.'.format(kwh * 0.40))
    else:
        print('O valor a ser pago é {:.2f} reais.'.format(kwh * 0.65))

if tipo == 'Comercial':
    if kwh <= 1000:
        print('O valor a ser pago é {:.2f} reais.'.format(kwh * 0.55))
    else:
        print('O valor a ser pago é {:.2f} reais.'.format(kwh * 0.60))
        
if tipo == 'Industrial':
    if kwh <= 5000:
        print('O valor a ser pago é {:.2f} reais.'.format(kwh * 0.55))
    else:
        print('O valor a ser pago é {:.2f} reais.'.format(kwh * 0.60))
    