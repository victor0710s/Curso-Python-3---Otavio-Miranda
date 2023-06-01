'''
Função lambda em Python
    A função lambda em Python é uma função como qualquer
    outra em Python. Porém, são funções anônimas
    que contém apenas uma linha. Ou seja, tudo
    deve ser contido dentro de uma uma única expressão.

    lista = [
        {'nome': 'Luiz', 'sobrenome': 'Miranda'},
        {'nome': 'Victor', 'sobrenome': 'Silva'},
        {'nome': 'Maria', 'sobrenome': 'Oliveira'},
        {'nome': 'Daniel', 'sobrenome': 'Silva'},
        {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    ]

'''

# lista = [1, 65, 23, 2, 7, 5, 34, 98]
# lista.sort()
# sorted(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Victor', 'sobrenome': 'Silva'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
]

# Funcao comum para ordernar a lista:
# def ordena(item):
# return item['nome']

# lista.sort(key=ordena)
# print(list)

# Funcao anônima(lambda):
# Mesma funcionalidade que a função ordena
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])


def exibir(lista):  # Imprimir a lista ordenada por item
    for item in lista:
        print(item)
    print()


exibir(l1)
exibir(l2)
