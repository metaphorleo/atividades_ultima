#definindo funcao que retorna valor booleano ao checar se o prefixo de duas strings sao iguais
def prefixo(palavra1, palavra2):
    comparar = palavra1.startswith(palavra2)
    return comparar

teste = prefixo("telhado", "telha")

print(teste)