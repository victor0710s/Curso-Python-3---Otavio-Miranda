# Empacotamento e desempacotamento de dicionarios

a, b = 1, 2
a, b = b, a

# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# .values() retorna os valores do dicionario
# a, b = pessoa.values()

# .keys() retorna as o nome das chaves do dicionario
# a, b = pessoa.keys()

# .items() retorna os items dentro do dicionario (chaves e valores)
# a, b = pessoa.items()
# print(a, b)

# Da pra fazer desempacomenteo interno usando o .items(). EX:
# (a1, a2), (b1, b2) = pessoa.items()
# print('{} => {}'.format(a1, a2))
# print('{} => {}'.format(b1, b2))

# for k, v in pessoa.items():
#     print(k, v)

dados_pessoa = {
    'idade': 167,
    'altura': 1.6,
}

pessoa_completa = {
    **pessoa, **dados_pessoa
}
# print(pessoa_completa)

# args e kwargs
# args (ja vimos)
# kwargs keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados =>', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=1234)
# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)
