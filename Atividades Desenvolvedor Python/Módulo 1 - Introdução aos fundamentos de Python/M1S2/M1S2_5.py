while True:
    try:
        Gênero = float(input("Insira 1 para Homem ou 2 para Mulher: "))
        if Gênero == 1:
            try:
                altura = float(input("Insira a altura em metros(apenas números): "))
            except ValueError:
                print("Insira um valor numérico.")
            else:
                ideal_homem = 72.7 * altura - 58
                print(f"O peso ideal de um homem com {altura} m de altura é de {ideal_homem:.1f} kg.")
                break
        elif Gênero == 2:
                try:
                    altura = float(input("Insira a altura em metros(apenas números): "))
                except ValueError:
                    print("Insira um valor numérico.")
                else:
                    ideal_mulher = 62.1 * altura - 44.7
                print(f"O peso ideal de uma mulher com {altura} m de altura é de {ideal_mulher:.1f} kg.")
                break
    except ValueError:
        print("Valor inválido.")
    else:
        print("Número inválido.")