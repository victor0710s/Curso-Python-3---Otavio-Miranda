# Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  # Tem __iter__ e __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))  # Vai gerar erro pois acabou a lista de itens do iterator
