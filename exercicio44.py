p = float(input('Qual o valor do produto? R$'))
print('''Selecione uma forma de pagamento:
[1] Á vista (Dinheiro / Cheque)!
[2] Á vista no Cartão!'
[3] Em até 2x no Cartão!
[4] 3x ou mais no Cartão!''')
e=str(input('Qual sua escolha?'))
if e == '1':
    desc = 10
    final = p - (p /100 * desc)
    print('Pagando a vista (Dinheiro / Cheque) o desconto será de {}%, o preço final do produto será R${:.2f} reais!'.format(desc,final))
elif e == '2':
    desc = 5
    final = p - (p /100 * desc)
    print('Pagando a vista no Cartão o desconto será de {}%, o preço final do produto será R${:.2f} reais!'.format(desc,final))
elif e == '3':
    desc = 0
    final = p - (p /100 * desc)
    print('Em até 2x no Cartão não hávera desconto, o preço final do produto será R${:.2f} reais!'.format(final))
elif e == '4':
    juros = 20
    final = p + (p /100 * juros)
    parcelas = int(input('Deseja quantas parcelas?'))
    print('Em 3x ou mais no Cartão seu juros será de {}%, o preço final do produto será R${:.2f} reais!'.format(juros,final))
    print('Sendo {} parcelas ,cada parcela terá o valor de {:.2f} reais!'.format(parcelas,final/parcelas))
else:
    print('Opção invalida , reinicie o processo!')
