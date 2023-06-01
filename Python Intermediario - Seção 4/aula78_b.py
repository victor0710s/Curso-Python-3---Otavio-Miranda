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
import copy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}
# Faz uma cópia rasa mas não alcança subniveis como a lista 'l1' a nao ser que se use o deepcopy()
d2 = copy.deepcopy(d1)
d3 = d2.copy()

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)
print(d3)
