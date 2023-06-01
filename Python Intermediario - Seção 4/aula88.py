# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)

lista = [0]
dicionario = {}
conjunto = {}
tupla = ()
string = ""
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(2)


def falsy(valor):
    return 'falsy' if not valor else 'truthy'


# Tudo o que nao tiver nenhum valor como por exemplo uma lista vazia retorna falsy
print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))
