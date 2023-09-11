'''
4)	Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
'''
nome = str(input('Digite o seu nome: '))
salario = float(input('Digite o seu salário aqui: '))
porcentagem = int(input('Digite um número que aumentara do salário em porcentagem: '))
aumento = salario + (salario * porcentagem) / 100
print('O seu nome é {}. \nO seu salário atual é {:.2f} reais. \nVocê teve um aumento de {}% no seu salário atual. \nO seu novo salário é {:.2f} reais.'.format(nome, salario, porcentagem, aumento))
