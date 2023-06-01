'''
    Retorno de valores da funções (return)

    Diferente do print() que ao inves de retornar um valor e futuramente voce poder usa-lo
    o print() so mostra o valor no sistema, já o return retorna um valor "funcional" para que seja 
    usado depois. Somente funções e métodos possuem o return. Assim que for encontrado um return
    dentro de uma função o codigo para e tudo apos ele (return) nao sera executada
'''


def soma(x, y):
    if x > 10:
        return 10, 20
    return x + y
    print('Estou depois do return e nao vou ser executado')


soma1 = soma(2, 4)
soma2 = soma(2, 2)
print(soma1)
print(soma2)
print(soma(11, 10))
