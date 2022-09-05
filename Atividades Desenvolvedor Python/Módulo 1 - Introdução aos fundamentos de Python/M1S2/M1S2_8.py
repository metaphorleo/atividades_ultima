#definindo a mensagem criptografada e gerando uma variavel vazia para posteriormente concatenar as letras descriptografadas
mensagem_criptografada = ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']
codigo_letra = ''
palavra = ''

#concatenando dois elementos da lista para formar um numero de dois algarismos, ignorando o "-1"(definido como intervalo no exercicio) e entao convertando cada numero em um caracter alfabetico ASCII
for h in mensagem_criptografada:
    if h != '-1':
        codigo_letra += h
    else:
        palavra += chr(int(codigo_letra))
        codigo_letra = ''

print(palavra)