n1=int(input('Digite um numero:'))
n2=int(input('Digite um segundo numero:'))

if n1>n2:
    print('O numero {} é maior que {}!'.format(n1,n2))
elif n2>n1:
    print('O numero {} é maior que {}!'.format(n2,n1))
else:
    print('\033[31mOs valores são iguais!\033[m')
