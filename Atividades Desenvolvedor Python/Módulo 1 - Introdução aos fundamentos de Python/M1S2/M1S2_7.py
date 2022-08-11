while True:
    try:
        preço_produto = float(input("Digite o preço do produto (apenas números): "))
        print("À vista em dinheiro, recebe 15% de desconto = 1")
        print("À vista no cartão de crédito, recebe 10% de desconto = 2")
        print("Em duas vezes, preço normal de etiqueta sem juros = 3")
        print("Mais de duas vezes, preço normal de etiqueta mais juros de 10% = 4")
        try:
            método_pgt = float(input("Digite o método de pagamento (1 a 4): "))
        except ValueError:
            print("Valor inválido")
        if método_pgt == 1:
            preço_1 = preço_produto - preço_produto * 0.15
            print(f"O preço a ser cobrado é R$ {preço_1:.2f}.")
            break
        elif método_pgt == 2:
            preço_2 = preço_produto - preço_produto * 0.1
            print(f"O preço a ser cobrado é R$ {preço_2:.2f}.")
            break
        elif método_pgt == 3:
            preço_3 = preço_produto / 2
            print(f"O preço a ser cobrado é 2x de R$ {preço_3:.2f}.")
            break
        elif método_pgt == 4:
            try:
                parcelas = int(input("Digite em quantas vezes será parcelado (apenas números): "))
            except ValueError:
                print("Valor inválido.")
            preço_4 = (preço_produto / parcelas) + (preço_produto / parcelas) * 0.1
            total_4 = preço_4 * parcelas
            print(f"O valor a ser cobrado é {parcelas}x de R$ {preço_4:.2f}, totalizando R$ {total_4:.2f}.")
            break
        else:
            print("Número inválido.")
    except ValueError:
        print("Valor inválido.")