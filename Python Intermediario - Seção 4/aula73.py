'''
    Higher Order Functions
    Funções de Primeira Classe
'''


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Victor')
)

print(
    executa(saudacao, 'Bom dia', 'Menina do Sonho')
)
