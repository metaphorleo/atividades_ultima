while True:
    try:
        A = float(input("Insira o valor numérico de A: "))
    except ValueError:
            print("O valor de A dever ser um número.")
    else:
        break

while True:
    try:
        B = float(input("Insira o valor numérico de B: "))
    except ValueError:
            print("O valor de B dever ser um número.")
    else:
        break

while True:
    try:
        C = float(input("Insira o valor numérico de C: "))
    except ValueError:
            print("O valor de C dever ser um número.")
    else:
        break

soma_ab = A + B

if soma_ab > C:
    print(f"A soma de A + B é {soma_ab}.")
else:
    print("A soma A + B é menor que C.")