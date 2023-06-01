# Introdução às Generator Functions em Python
# generator = (n for n in range1(1000))

def generator(n=0):  # Generator function
    yield 1
    print('Continuando...')
    yield 2
    print('Continuando...')
    yield 3
    print('Teminou...')
    return "ACABOU"


gen = generator(n=0)
for n in gen:  # Melhor do que usar o next() varias vezes
    print(n)
