# Try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('ABRIU ARQUIVO')
    # 8 / 0
except ZeroDivisionError as e:
    print(e.__class__.__name__, '->', e)
else:
    print('Não deu erro')
finally:
    print('FECHOU ARQUIVO')
