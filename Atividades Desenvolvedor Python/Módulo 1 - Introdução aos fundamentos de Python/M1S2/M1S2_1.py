cent_5 = 0.05
cent_10 = 0.10
cent_25 = 0.25
cent_50 = 0.50
real_1 = 1

qtd_cent5 = 35
qtd_cent10 = 50
qtd_cent25 = 30
qtd_cent50 = 15
qtd_real1 = 19

total_cent5 = (cent_5 * qtd_cent5)
total_cent10 = (cent_10 * qtd_cent10)
total_cent25 = (cent_25 * qtd_cent25)
total_cent50 = (cent_50 * qtd_cent50)
total_real1 = (real_1 * qtd_real1)

total_caixa = (total_cent5 + total_cent10 + total_cent25 + total_cent50 + total_real1)

print(f"O caixa do bar do Sr. João possui R$ {total_caixa}.")