'''
12)	Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('='*70)
print('Quando for digitar a operação que dejesa, use os símbolos mostrados ou o nome da operação.')
print('Operações disponiveis: \nsoma (+) \nsubtração (-) \nmultiplicação (*) \ndivisão (/)')
print('='*70)
operacao = str(input('Digite qual operação quer usar: '))

if operacao == '+' or 'soma':
    print('A soma dos números {} e {} é igual a {}.'.format(n1, n2, n1 + n2))

if operacao == '-' or 'subtração':
    print('A subtração dos números {} e {} é igual a {}.'.format(n1, n2, n1 - n2))

if operacao == '*' or 'multiplicação':
    print('A multiplicação dos números {} e {} é igual a {}.'.format(n1, n2, n1 * n2))

if operacao == '/' or 'divisão':
    print('A divisão dos números {} e {} é igual a {}.'.format(n1, n2, n1 / n2))