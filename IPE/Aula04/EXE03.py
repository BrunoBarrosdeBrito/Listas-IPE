'''
3)	Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
'''
tempo = int(input('Digite um número, que sera transformado em segundos, minutos, horas e dias: '))
seg = tempo
min = seg / 60
horas = seg / 3600
dias = seg / 86400
print('Em segundos é: {} segundos. \nDe segundos para minutos é {} minutos. \nDe segundos para horas é {} horas. \nDe segundos para dias é {} dias.'.format(seg, min, horas, dias))
