# from sys import path

# import aula99_package.modulo
# from aula99_package import modulo
# from aula99_package.modulo import *

# Formas de usar os modulos e suas funcoes...
# print(soma(2, 3))
# print(aula99_package.modulo.soma(2, 3))
# print(modulo.soma(2, 3))
# print(var)
# print(new_var) # Vai dar erro pois nao foi instanciada no modulo para ser importada

# from aula99_package.modulo import fala_oi, soma

# print(__name__)
# fala_oi('Victor')

from aula99_package import fala_oi, soma

print(soma(15, 98))
fala_oi('Victor')
