# __all__ = [
#     'var',
#     'soma'
# ]

# Poderia ser importado como .modulo_b pois mesmo q mude o nome da pasta raiz na terá problemas
# from aula99_package.modulo_b import fala_oi
var = 'Victor'


def soma(x, y):
    return x + y


new_var = 'Nova Variavel'  # Nao vai poder ser usada pois nao foi colocada em __all__

# fala_oi()
