# Try, except, else e finally

try:
    a = 10
    b = 0
    # print(b[0])
    print('linha 1'[1000])
    c = a / b
    print('linha 2')

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')  # comentar variavel b para funcionar
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')  # descomentar print(b[0])
    print('Nome ERRO:', error.__class__.__name__)
    print('MSG:', error)
except Exception:
    print('!! Erro Desconhecido !!')
