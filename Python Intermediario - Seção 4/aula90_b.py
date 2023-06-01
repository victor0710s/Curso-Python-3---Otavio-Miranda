# Generator expression, Iterables e Iterators em Python
import sys  # Importamos o modulo sys somente para ver o tamanho ocupado na memoria

# iterator
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  # Tem __iter__ e __next__

# generator
lista = [n for n in range(100)]
generator = (n for n in range(100))  # Generator expression

print(lista)
print(generator)

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# Generator entra a medida que preciso enquanto a lista entrega tudo de uma vez
