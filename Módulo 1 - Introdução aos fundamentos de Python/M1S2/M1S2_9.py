#definindo mensagem criptografada
mensagem_criptografada = "HVWRX HPSROJDGR FRP R FXUVR GH SBWKRQ"

#definindo variavel vazia para concatenacao da frase
msg_decifrada = ""

#transformando a string em uma lista para separar cada caracter
msg_lista = list(mensagem_criptografada)

#definindo chave da cifra de Cesar dada pelo exercicio
chave = 3

#convertendo cada letra alfabetica em um numero ASCII, aplicando a chave enquanto ignora as barras de espaco (32) e limita o inicio e fim do alfabeto (26 letras) e, por fim, convertendo de volta o numero obtido em um caracter alfabetico
msg_num = [ord(i) for i in msg_lista]
for i in msg_num:
    if i != 32 and i >= 68:
        msg_decifrada += chr(i - chave)
    elif i != 32 and i < 68:
        msg_decifrada += chr(i + 26 - chave)
    else:
        msg_decifrada += " "

print(msg_decifrada)