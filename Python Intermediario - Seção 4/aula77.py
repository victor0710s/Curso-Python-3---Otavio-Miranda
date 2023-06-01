# Manipulando chaves e valores em dicionários

pessoa = {}

# Nao é possicek acessar indices inexistentes e nem chave/valor com nomes errados.
# EX: chave_1 = 'Ola'
# print(chave) = Vai gerar um erro pois o chave requerida nao foi encontrada!

# pessoa['nome'] = 'Victor da Silva'


chave = 'nome'

pessoa[chave] = 'Victor da Silva Santos'
pessoa['sobrenome'] = 'Augusto'

print(pessoa[chave])

pessoa[chave] = 'Joao'

del pessoa['sobrenome']  # Deleta a chave/valor entre [ ]
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Nao Exite!')

else:
    print(pessoa['sobrenome'])
