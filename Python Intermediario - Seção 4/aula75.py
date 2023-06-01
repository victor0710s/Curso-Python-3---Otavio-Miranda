'''
    Exercicios:
        Crie funções que duplicam, triplicam e quadruplicam
        o numero recebido como parametro
'''


def criar_multiplicador(multiplicador):
    def multiplicar(n):
        return n * multiplicador
    return multiplicar


dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)
quad = criar_multiplicador(4)

print(dobro(2))
print(triplo(2))
print(quad(2))
