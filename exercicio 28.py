from random import randint
from time import sleep
n= randint(0, 5)
print('-=-' * 20)
print('Advinhe o meu número, ele varia de 0 a 5!')
print('-=-' * 20)
r=int(input('Em que número eu pensei?'))
print('Wait a second... Loading...')
sleep(3)
if n == r:
    print('Ninja, acertou mizeravi!')
else:
    print('Try again bicth! meu numero é {}! e não {}'.format(n ,r))
print('Fim do jogo!')