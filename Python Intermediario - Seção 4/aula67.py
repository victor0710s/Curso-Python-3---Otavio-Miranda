'''
    Valores padrão para parametros
    Ao definir uma função, os parametros podem ter 
    valores padrão. Caso o valor não seja enviado
    para o parametro, o valor padrão será
    usado.
    Refatorar: editar seu código afim de otimiza-lo.
'''


def soma(x, y, z=None):  # Z nomeado com none para caso eu queira usar outro valor para ele ou nao
    if z is not None:  # Condicao para verificar se z tem o valor padrão ou outro passado atribuido a ele
        print(f'{x=} {y=} {z=} ', '|', 'x + y + z =', x + y + z)
    else:  # Se z continuar sendo None será mostrado o resultado "sem" o z
        print(f'{x=} {y=} ', '|', 'x + y = ', x + y)


soma(1, 2)
soma(3, 15)
soma(100, 250)
soma(2, 4, 6)
soma(1, 2, z=0)  # Apesar de zero ser um False quando usado no if o valor padrao para a condicao é o none, entao ele acaba por se tornar "True"
