def p_ou_n(num):
    if num >= 1:
        return "P"
    return "N"

numero = p_ou_n(-1)

print(numero)