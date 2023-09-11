'''
11)	Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
'''
viagem = int(input('Digite a distância da viagem em KM: '))
if viagem <= 200:
    print('A sua viagem irá custar {:.2f} reais.'.format(viagem * 0.50))
else:
    print('A sua viagem irá custar {:.2f} reais.'.format(viagem * 0.45))