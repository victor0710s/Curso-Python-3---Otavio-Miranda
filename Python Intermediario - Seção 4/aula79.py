'''
    * Sets - Conjuntos em Python (tipo set)
    * Conjuntos são ensinados na matemática
    * link_ref = https://brasilescola.uol.com.br/matematica/conjunto.htm
    * Representados graficamente pelo diagrama de Venn
    * Sets em python são mutáveis, porém aceitam apenas
    tipos imutáveis como valores interno.

'''

# Criando um set
# set(iteravel) ou {1, 2, 3}
# s1 = set() -> melhor se for enviado tuplas, listas etc
# s1 = {'Victor', 1, 2, 3}  # com dados
# s2 = set()  # sem dados
# print(s1, type(s1))


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)  # -> filtragem de items repetidos
# l2 = list(s1)
# s1 = {1, 2, 3}
# # print(4 in s1)
# for numero in s1:
#     print(numero)


# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz')  # -> adiciona um valor ao set
s1.add(1)

# atualiza os dados de um set igual no dicionário
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear() # -> apaga tudo dentro do set
s1.discard('Olá mundo')  # -> discarta o valor escolhido dentro da func
s1.discard('Luiz')
# print(s1)


# Operadores úteis:
# união | união (union) - une
# intersecção & (intersection) - items presentes em ambos
# diferença - items presentes apenas no set da esquerda
# diferença simétrica ^ - Items que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)
