a=float(input('Qual o sálario base?'))
b=float(input('Qual o aumento em %?' ))
c=a+((a/100)*b)
print('O salário original de R${:.2f} reais, com aumento de {:.2f}% ficará em R${:.2f} reais.'.format(a ,b, c))