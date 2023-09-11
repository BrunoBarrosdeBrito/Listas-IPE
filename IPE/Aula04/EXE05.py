'''
5)	Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
'''
produto = str(input('Digite o nome de um produto: '))
valor = float(input('Digite o valor do produto: '))
porcentagem = int(input('Digite o número do desconto do produto: '))
desconto = valor - (valor * porcentagem) / 100
print('O produto é o {}. \nO valor atual do produto é {:.2f} reais. \nE com o desconto de {}%, o novo valor a ser pago por esse produto é {:.2f} reais'.format(produto, valor, porcentagem, desconto))