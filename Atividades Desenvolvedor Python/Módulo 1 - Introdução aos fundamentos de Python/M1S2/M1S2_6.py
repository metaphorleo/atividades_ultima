while True:
    try:
        peso = float(input("Insira o peso do paciente em kg (apenas números e vírgula): "))
        try:
            altura = float(input("Insira a altura do paciente em m (apenas números e vírgula): "))
        except ValueError:
            print("Valor inválido.")
        imc = peso / altura ** 2
        if imc < 18.5:
            print(f"O IMC do paciente é {imc:.1f} (Abaixo do peso).")
            break
        elif imc < 25:
            print(f"O IMC do paciente é {imc:.1f} (Peso normal).")
            break
        elif imc < 30:
            print(f"O IMC do paciente é {imc:.1f} (Acima do peso).")
            break
        elif imc > 30:
            print(f"O IMC do paciente é {imc:.1f} (Obeso).")
            break
    except ValueError:
        print("Valor inválido.")