# dir, hasattr e getattr em Python

string = 'Victor'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    # Procurando o metedo o upper dentro de metodo e logo em seguinda o executando
    print(getattr(string, metodo)())
else:
    print('Não existe este método', metodo)
