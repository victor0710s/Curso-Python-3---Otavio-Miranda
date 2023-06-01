# Introdução às Generator Functions em Python
# generator = (n for n in range1(1000))

# Agora iremos fazer como se fosse o range

def generator(n=0, maximum=10):  # Generator function
    while True:
        yield n  # o yield "pausa" o while igual o input
        n += 1

        if n >= maximum:
            return


# podemos definir aqui o valor que queremos gerar
gen = generator(maximum=10000)
for n in gen:  # Melhor do que usar o next() varias vezes
    print(n)
