'''
    Métodos úteis dos dicionários em Python:

        len - quantas chaves
        keys - iterável com as chaves
        values - iterável com os valores
        items - iterável com chaves e vlaores
        setdefault - adiciona valor se a chave não existe
        copy - retorna uma cópia rasa (shallow copy)
        get - obtém uma chave
        pop - apaga um item com a chave especificada (del)
        popitem - apaga o último item adicionado
        update - atualiza um dicionário com outro

'''

pessoa = {
    'nome': 'Victor da Silva',
    'sobrenome': 'Santos',
    # 'idade': 20,
}

pessoa.setdefault('idade', 'Não possui idade ainda.')
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))


# for valor in pessoa.values():
#     print(valor)

# for k, v in pessoa.items():
#     print(k, v)
