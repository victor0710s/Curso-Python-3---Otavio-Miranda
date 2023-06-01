# Exercicios com Funções

'''
    Crie um função que multiplica todos
    os argumentos nao nomeados recebidos.
    Retorne o total para uma variavel e mostre
    o valor da variavel.

'''


def multi(*args):
    total = 1
    for n in args:
        total = total * n
    return total


multiplica = multi(4, 5, 6, 7)
print(multiplica)
print('Conferindo: ', 4*5*6*7)


'''
    Crie uma função que fala se um número 
    é par ou ímpar. Retorne se o numero é par ou ímpar.
'''


def par_ou_impar(n):
    if n % 2 == 0:
        return 'O numero é par'
    return 'O numero é ímpar'


numero = par_ou_impar(14)
print(numero)
