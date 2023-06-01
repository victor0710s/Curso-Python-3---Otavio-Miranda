import importlib
import aula98_m

print(aula98_m.var)

for i in range(10):
    # Serve para recarregar todo o modulo novamente atualizando mudancas e etc
    importlib.reload(aula98_m)
    print(i)

print('Fim!')
