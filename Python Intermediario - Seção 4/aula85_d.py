lista = []
for x in range(3):  # A cada 3 x haverá 3 y
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y)
    # Mesma coisa que antes mas agora usando list comprehension
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x, letra) for letra in 'Victor']
    for x in range(3)
]
print(lista)

# Video explicando melhor sobre o list comprehension: https://www.youtube.com/watch?v=1YbTDczvqco
