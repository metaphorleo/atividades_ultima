def somatorio(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma = somatorio(1, 2, 3, 4)

print(soma)