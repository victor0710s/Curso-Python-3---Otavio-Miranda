'''
    Escopo de funções em Python
    Escopo significa o local onde aquele código pode atingir.
    Existe o escopo global e local.
    O escopo global é o escopo onde todo o código é alcançavel.
    O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcaçados.
    Nao temos ascessos aos nomes de escopo internos nos escopos externos.
    A palavra global faz uma variavel do escopo externo ser a mesma 
    de um escopo interno.
'''

# Escopo do modulo / arquivo
x = 1


def escopo():  # Escopo da função escopo()
    # global x  # "Permissao" para que a função modifique o valor de x dentro e fora de seu escopo
    x = 10

    def outra_funcao():  # Escopo da função outra_funcao()
        # global x  # "Permissao" para que a função modifique o valor dentro e fora de seu escopo
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)  # x = 1
escopo()  # Chamando a função escopo() / x = 11 pois chama a outra_funcao() primeiro
print(x)  # x = 11

'''
    x = 1 pertence ao escopo do modulo / arquivo, ou seja, pode ser
    acessado de qualquer lugar do código. Já a função escopo() possui
    seu proprio escopo, onde dentro dela existe a outra_função()
    que tambem possui seu proprio escopo. Dentra da outra_função() existe
    uma variavel chamada y onde somente pode ser acessada pela função que possui o 
    escopo onde se encontra esta variavel, mas esta mesma funcao pode acessar
    tudo que está fora dela em camada mais proximas ao escopo do modulo
    mas as mesmas nao podem acessar dentro dela.

    Ao adicionar o global x estou dando permissao para outros escopos modificarem o
    valor dessa variavel.
'''
