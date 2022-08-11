import time
class caixa_eletronico:
    def __init__(self):
        input("--------------------------------------------------\nBem vindo ao Caixa Eletrônico Python!\nAperte qualquer tecla para continuar: ")
        print("--------------------------------------------------\nEscolha um serviço: \n > Depósito \n > Saque \n > Extrato \n > Outros serviços")
        time.sleep(0.6)
        print("> Saque\n--------------------------------------------------")
        time.sleep(0.6)
        self.saque()

    def saque(self):
        sacar = "S"
        while sacar == "S" or sacar == "s":
            try:
                print("Notas disponíveis:   > R$ 100   > R$ 50   > R$ 20   > R$ 10")
                valor_saque = int(input("Digite um valor para sacar: R$ "))
                time.sleep(0.6)
                if valor_saque % 10 == 0:
                    cem = valor_saque // 100
                    cinquenta = ((valor_saque % 100) % 100) // 50
                    vinte = (((valor_saque % 100) % 100) % 50) // 20
                    dez = ((((valor_saque % 100) % 100) % 50) % 20) // 10
                    print(f"Você recebeu R$ {valor_saque} em:")
                    if cem > 0:
                        print(f"> {cem} nota(s) de R$ 100")
                    if cinquenta > 0:
                        print(f"> {cinquenta} nota(s) de R$ 50")
                    if vinte > 0:
                        print(f"> {vinte} nota(s) de R$ 20")
                    if dez > 0:
                        print(f"> {dez} nota(s) de R$ 10")
                    time.sleep(0.3)
                    sacar = input("Deseja realizar outra transação?\n Sim = S     Não = Pressione qualquer tecla\nS/N: ")
                else:
                    raise ValueError
            except ValueError:
                print("Valor inválido, digite novamente.\n--------------------------------------------------")
                time.sleep(0.6)
        print("O Banco Python agradeçe, volte sempre!")
        time.sleep(1.2)
        caixa_eletronico()

caixa_eletronico()