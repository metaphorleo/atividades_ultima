mensagem_criptografada = ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']
codigo_letra = ''
palavra = ''

for h in mensagem_criptografada:
    if h != '-1':
        codigo_letra += h
    else:
        palavra += chr(int(codigo_letra))
        codigo_letra = ''

print(palavra)