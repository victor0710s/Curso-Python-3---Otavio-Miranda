# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preço': 2.5,
    'categoria': 'Escritório',
}

# for chave, valor in produto.items():
# print(chave, valor)

dic = {
    # Para cada chave eu tenho um valor e assim consigo usar o for dentro do dict
    chave: valor.upper()
    # isinstance checa se um parametro é de determinado tipo
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
    ('d', 'valor d'),
]
dc = {
    chave: valor
    for chave, valor in lista
}
# print(dic)
# print(dc)

set_1 = {i for i in range(10)}
print(set_1)
