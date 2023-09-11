'''
10)	Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%
'''
salario = float(input('Digite o seu salário atual:R$ '))
if salario > 1250.50:
    print('O seu salário atual é {:.2f} reais, e teve um aumento de 10%. \nEntão o seu novo salário é {:.2f} reais.'.format(salario, salario + (salario * 10)/ 100))
else:
    print('O seu salário atual é {:.2f} reais, e teve um aumento de 15%. \nEntão o seu novo salário é {:.2f} reais.'.format(salario, salario + (salario * 15)/ 100))
