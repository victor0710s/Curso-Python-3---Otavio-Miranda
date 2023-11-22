# copy, sorted, produtos.sort
import copy

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

"""
Ex: pegou o lista contendo o dict produtos e expandiu ele na var **p e criou denovo a chave preco
passando como valor o value da chave preco da lista produtos + 10%. O round serviu para deixa com 2 casa decimais
"""

#############################################################################################

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

"""
Ex: primero faz a copia da lista produtos, segundo usa a funcao lambda pra criar um produto p e depois ordenar a criacao
pelo nome do produto 'Produto 1....' e o reverse inverte a ordem deixando decrescente.
"""

#############################################################################################

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)

"""
Ex: primero faz a copia da lista produtos, segundo usa a funcao lambda pra criar um produto p e depois ordenar a criacao
pelo valor do produto.
"""

## Resultados ##
print('Original')
print(*produtos, sep='\n')
print()
print('Resposta 1')
print(*novos_produtos, sep='\n')
print()
print('Resposta 2')
print(*produtos_ordenados_por_nome, sep='\n')
print()
print('Resposta 3')
print(*produtos_ordenados_por_preco, sep='\n')
