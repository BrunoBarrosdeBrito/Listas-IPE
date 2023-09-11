'''
1) Exercício: Faça um algoritmo que:
b) Sabendo que a quantidade de alunos na turma de PYTHON é igual a 32, faça uma estrutura condicional onde verifique se o número é maior que 30; neste caso, estes ganharão uma passagem para Cancun. Se for igual a 30, estes ganharão uma passagem para Fortaleza. Se for menor que 30, estes ganharão uma passagem para Caldas Novas. 
'''
qtd_alunos = 32
if qtd_alunos > 30:
    print('Os alunos da turma de Python ganharam uma viagem para Cancun.')
else:
    if qtd_alunos == 30:
        print('Os alunos da turma de Python ganharam uma viagem para Fortaleza.')
    else:
        print('Os alunos da turma de Python ganharam uma viagem para Caldas Novas.')