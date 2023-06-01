'''
    Argumentos nomeados e não nomeados em funções Python
    Argumento nomeado tem nome e sinal de igual
    Argumento não nomeador recebe somente o argumento (valor)
'''


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} z={z}', '|', 'x + y + z = ', x + y + z)


soma(2, 3, 4)  # argumento posicional
soma(2, 3, z=10)  # argumento nomeado
# Quando houver um argumento nomeado todos apos ele devem ser nomeados tbm para que nao de um erro.
# Sempre o argumento posicional vem antes do nomeado!!
