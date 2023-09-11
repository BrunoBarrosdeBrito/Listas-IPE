'''
8)	Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
'''
velo = int(input('Digite a velocidade do seu carro: '))
if velo > 80:
    print('Você foi multado por excesso de velocidade, o valor a ser pago é {:.2f} reais.'.format((velo - 80)*5))
else:
    print('Você não foi multado.')