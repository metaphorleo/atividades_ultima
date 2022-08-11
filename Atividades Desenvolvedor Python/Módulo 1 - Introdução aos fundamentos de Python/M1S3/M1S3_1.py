def par_impar(**kwargs):
    for ordem, numero in kwargs.items():
        if numero % 2 == 0:
            print(f"{ordem} - {numero} é par.")
        else:
            print(f"{ordem} - {numero} é ímpar.")

par_impar(n1= 1, n2= 2, n3 = 4)