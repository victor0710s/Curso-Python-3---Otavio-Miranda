'''
List comprehension em Python:
    List comprehension é uma forma rápida para criar listas a partir de itéraveis.

'''
# print(list(range(10)))  # formando uma lista básica usando print()

# Usando laco for:
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

# Usando list comprehension:
lista = [
    numero * 2 for numero in range(10)
]
print(lista)
