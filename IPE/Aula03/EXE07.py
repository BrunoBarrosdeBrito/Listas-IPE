'''
7) Faça um algoritmo que escreva seu nome, endereço e número da sua casa. Se o número de sua casa for menor que 65, escrever na tela que: você pagará o IPTU deste ano parcelado em 3 vezes; se for igual a 65, você pagará o IPTU em duas parcelas; se for maior 65, você pagará o IPTU à vista. Converta para PYTHON.
'''
nome = str(input('Digite o seu nome: '))
endereco = str(input('Digite o seu endereço: '))
num_casa = int(input('Digite o número da sua casa: '))
print('O seu nome é {}. \nO seu endereço é {}.'.format(nome, endereco))
if num_casa < 65:
    print('Você pagará o IPTU deste ano parcelado em 3 vezes.')
else:
    if num_casa == 65:
        print('Você pagará o IPTU em duas parcelas.')
    else:
        print('Você pagará o IPTU à vista')