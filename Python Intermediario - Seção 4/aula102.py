# Variaveis livres + nonlocal  (locals, globals)

# def fora(x):
#     a = x

#     def dentro():
#         print(locals())
#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)
# print(dentro1())
# print(dentro2())

def concatenar(string):
    str_final = string

    def func_interna(valor_a_concatenar):
        nonlocal str_final  # Informa o python q essa var nao é desse escopo e ele procura por ela
        str_final += valor_a_concatenar
        return str_final
    return func_interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
