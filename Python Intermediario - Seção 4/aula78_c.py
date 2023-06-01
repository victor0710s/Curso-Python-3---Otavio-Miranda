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

p1 = {
    'nome': 'Victor',
    'sobrenome': 'Silva Santos',
}

# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# remov_ult_chave = p1.popitem()
# print(remov_ult_chave)
# print(p1)

# p1.update({
#     'nome': 'Um jeito',
#     'idade': 20
# })
# p1.update(nome='Outro jeito', idade=20)
tupla = (('nome', 'Outro jeito com tupla'), ('idade', 20))
lista = [['nome', 'Outro jeito com lista'], ['idade', 20]]
p1.update(lista)

print(p1)
