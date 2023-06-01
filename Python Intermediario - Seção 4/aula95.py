# raise - Lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
# O raise "relança" o erro podendo assim indicar o que aconteceu sem ter que usar o bloco completo do try

# Funções de tratamento
def nao_pode_ser_zero(b):
    if b == 0:
        raise ZeroDivisionError("Você tentou dividir por zero!")
    return True


def tipo_errado(var):
    tipo_var = type(var).__name__  # Pega o nome do tipo da var
    # Verfica se a var é do tipo/instancia float ou int
    if not isinstance(var, (float, int)):
        raise TypeError(
            f'"{var}" deve ser int ou float. '
            f'Tipo <{tipo_var}> enviado.'
        )


# Função principal
def divide(a, b):
    nao_pode_ser_zero(b)
    tipo_errado(a)
    tipo_errado(b)
    return a / b


print(divide(10, '0'))
