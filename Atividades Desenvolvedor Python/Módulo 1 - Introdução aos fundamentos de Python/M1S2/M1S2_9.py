mensagem_criptografada = "HVWRX HPSROJDGR FRP R FXUVR GH SBWKRQ"

msg_decifrada = ""

msg_lista = list(mensagem_criptografada)

msg_num = [ord(i) for i in msg_lista]

for i in msg_num:
    if i != 32 and i >= 68:
        msg_decifrada += chr(i - 3)
    elif i != 32 and i < 68:
        msg_decifrada += chr(i + 26 - 3)
    else:
        msg_decifrada += " "

print(msg_decifrada)