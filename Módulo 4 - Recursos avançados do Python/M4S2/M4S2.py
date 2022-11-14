#definindo o decorator para indicar os nomes dos parametros da funcao de juros
def decorator_imprimir(func):
    def interno(a, b, c):
        resultado = func(a, b, c)
        print(f"CAPITAL: {a} TAXA: {b} TEMPO: {c}")
        print(f"RESULTADO: {resultado}")
        return func(a, b, c)
    return interno

#definindo a funcao de juros
@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

#testando o código com "if __name__ == '__main__':" para evitar que o script seja executado quando a funcao for importada
if __name__ == '__main__':
    juros_simples(1000, 5, 6)