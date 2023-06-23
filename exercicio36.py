valor = float(input('Qual o valor da casa?'))
sal = float(input('Salário do comprador:'))
prazo =int(input('Qntde. de anos para o pagamento:'))
prest = valor / (prazo *12)
limite = sal/100*30
if prest <= limite:
    print('Emprestimo aprovado! com parcelas de {:.2f}!'.format(prest))
else:
    print('Negado a parcela de {:.2f} não cabe em seu orçamento!'.format(prest))

# end' ' permite continuar a linha com informaçoes da linha de baixo