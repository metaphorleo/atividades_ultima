def contagem(numero):
    print(numero)
    if numero == 0:
        return 0
    return numero - contagem(numero - 1)

contagem(10)