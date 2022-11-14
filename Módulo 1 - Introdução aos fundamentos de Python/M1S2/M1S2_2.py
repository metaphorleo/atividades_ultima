#definindo o valor hora e horas de servico prestado
valor_inicial = 1000
qtd_horas = 80
valor_hora = 20.45

#calculando o valor do servico prestado
valor_bruto = valor_inicial + qtd_horas * valor_hora

total = valor_bruto + valor_bruto * 0.15

print(f"O valor total a ser cobrado pelo projeto será R$ {total:.2f}.")