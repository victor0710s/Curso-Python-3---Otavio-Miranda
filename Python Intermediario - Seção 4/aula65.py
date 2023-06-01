'''
    Introdução as funções (def) em Python
    Funções são trechos de código usados para 
    replicar determinada açõao ao longo do seu código.
    elas podem receber valores para paramêtros (argumentos)
    e retornar um valor específico.
    Por padrão, funções Python retornam None (nada).
'''


# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Victor')
saudacao('Jason')
# Um erro ocorreria se fosse um argumento posicional pois é necessario um valor para o parametro.
saudacao()
