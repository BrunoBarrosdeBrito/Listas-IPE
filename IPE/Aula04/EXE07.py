'''
7)	Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''
km = float(input('Digite quantos kms foram rodados com o carro alugado: '))
dias = int(input('Digite quantos dias que você usou o carro alugado: '))
pagar = (60 * dias) + (0.15 * km)
print('O total a ser pago a usar o carro alugado é {} reais.'.format(pagar))