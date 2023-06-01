'''
    args - argumentos não nomeados
    * - *args (empacotamento e desempacotamento)
'''

# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for num in args:
        print('Total = ', total, '+', num)
        total += num
        print('Total = ', total)
    print(total)


soma(1, 2, 3, 4, 5, 6)
