# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())  # Adicionando letra ao set letras

    if 'v' in letras:
        print('Achouuu!')
        break

    print(letras)
