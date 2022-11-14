#definindo funcao que calcula a gorjeta (10%) de um valor"
def func(x):
    valor = float(x * 0.1) 
    return valor

gorjeta = func(110)

print(f"R$ {gorjeta:.2f}")