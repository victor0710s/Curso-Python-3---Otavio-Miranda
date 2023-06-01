# Yield from em generator functions

def gen1():  # GF 1
    print('Começou G1')
    yield 1
    yield 2
    yield 3
    print('Terminou G1')


def gen2(gen=None):  # GF 2
    print('Começou G2')
    if gen is not None:  # Verifica se o gen tem algo atribuido a ele ou nao
        yield from gen
    else:
        print('O gen é None')
    yield 4
    yield 5
    yield 6
    print('Terminou G2')


def gen3():
    print('Começou G3')
    yield 10
    yield 20
    yield 30
    print('Terminou G3')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()  # Exemplo do None
for n in g1:
    print(n)
print()
for n in g2:
    print(n)
print()
for n in g3:
    print(n)
print()
