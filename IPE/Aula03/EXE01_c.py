'''
1) Exercício: Faça um algoritmo que:
c) Verifique qual foi o valor de sua compra numa determinada loja (sugestão: R$ 637,78). Se o valor total for maior que R$ 150,00, pegar este valor, calcular o desconto de 10% e escrever na tela o novo valor total. Se for igual a R$ 150,00, calcular o desconto de 7% e escrever na tela o novo valor total. Se for menor que R$ 150,00, calcular o desconto de 4% e escrever na tela o novo valor total.
'''
compra = float(input('Digite o valor da sua compra: '))
if compra > 150.00:
    print('Parabéns! você ganhou 10% de desconto na sua compra. \nO novo valor a ser pago é {:.2f} reais.'.format(compra - (compra * 10)/ 100))
else:
    if compra == 150.50:
        print('Parabéns! você ganhou 7% de desconto na sua compra. \nO novo valor a ser pago é {:.2f} reais.'.format(compra - (compra * 7)/ 100))
    else:
        print('Parabéns! você ganhou 4% de desconto na sua compra. \nO novo valor a ser pago é {:.2f} reais.'.format(compra - (compra * 4)/ 100))