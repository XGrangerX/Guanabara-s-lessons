a=float(input('Qual o preço do produto?'))
b=int(input('Qual o desconto em %?' ))
c=a-((a/100)*b)
print('O produto que custava R${:.2f} reais, com desconto de {:.2f}% saíra por R${:.2f} reais.'.format(a ,b, c))