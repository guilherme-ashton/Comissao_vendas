#COmissão de vendas

venda = float(input('Insira o valor da venda feita: '))
comissao_1 = 700.00 + (venda * 0.16)
comissao_2 = 650.00 + (venda * 0.14)
comissao_3 = 600.00 + (venda * 0.14)
comissao_4 = 550.00 + (venda * 0.14)
comissao_5 = 500.00 + (venda * 0.14)
comissao_6 = 400.00 + (venda * 0.14)




if venda >= 100.000:
    print('A comissão a ser paga é de: R$ {0}' .format(comissao_1))
elif (venda < 100.000) and (venda >= 80.000):
    print('A comissão a ser paga é de: R$ {0}' .format(comissao_2))
elif (venda < 80.000) and (venda >= 60.000):
    print('A comissão a ser paga é de: R$ {0}' .format(comissao_3))
elif (venda < 60.000) and (venda >= 40.000):
    print('A comissão a ser paga é de: R$ {0}' .format(comissao_4))
elif (venda < 40.000) and (venda >= 20.000):
    print('A comissão a ser paga é de: R$ {0}' .format(comissao_5))
elif venda < 20.000:
    print('A comissão a ser paga é de: R$ {0}' .format(comissao_6))
else:
    print('Não há comissão a ser recebida')

