'''
List comprehension em Python:
    List comprehension é uma forma rápida para criar listas a partir de itéraveis.

'''
# print(list(range(10)))  # formando uma lista básica usando print()

import pprint  # Modulo para imprimir algo mais organizado


def p(v):  # Funcao para nao ter que escrever pprint toda hora
    pprint.pprint(v, sort_dicts=False, width=40)


# Usando laco for:
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

# Usando list comprehension:
lista = [
    numero * 2 for numero in range(10)
]
# print(list(range(10)))  # lista de 0 a 9
# print(lista)  # mesma lista mas com todos o numeros x2

# Mapeamento de dados em list comprehension:

produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },
]
novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
]
# print(novos_produtos)
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]
# print(lista)

novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
    if produto['preço'] > 10
]
p(novos_produtos)
