viagem=float(input('Qual a distância em quilometros da sua viagem?'))
p1=viagem * 0.5
p2=viagem * 0.45

if viagem < 200:
    print('Sua passagem custará R${:.2f} reais!'.format(p1))

else:
    print('Sua passagem custará R${:.2f} reais!'.format(p2))
print('Obrigado pela preferência')