'''
6)	Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para a conversão é:
'''
celsius = int(input('Digite em graus °C o número desejado para transformar em Fahrenheit: '))
Fahrenheit = ((9 * celsius) / 5) + 32
print('O valor em graus °C foi convertido para {:.0f} graus °F.'.format(Fahrenheit))