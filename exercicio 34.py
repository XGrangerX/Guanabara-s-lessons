sal = float(input('Qual o salário atual?'))
nsal = sal
if sal >= 1250:
    nsal = ((sal / 100)*10)+sal
if sal < 1250:
    nsal = ((sal / 100)*15)+sal
print('Com base no salário atual , após o aumento seu novo salário será de R${:.2f}.'.format(nsal))