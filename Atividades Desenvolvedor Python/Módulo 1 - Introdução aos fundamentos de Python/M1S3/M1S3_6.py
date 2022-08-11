def func(x):
    contagem = 0
    for letra in x:
        if letra == "l":
            contagem += 1
    return contagem

num_letras = func("Hello World!")

print(num_letras)