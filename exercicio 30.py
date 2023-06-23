from time import sleep
n=int(input('Diga me um numero...'))
r= n % 2
print('Analizando...')
sleep(2.5)
if r == 0:
    print('Esse número é PAR!')
else:
    print('Esse número é IMPAR!')
