from time import sleep
from random import choice

print('\033[35m+\033[m' * 21)
print('\033[1;31mQUE COMECEM OS JOGOS\033[m')
print('\033[35m+\033[m' * 21)
sleep(2)
print('\033[34;1mINICIANDO...\033[m')
sleep(2)
print('\033[1;31mSerá que é capaz de me vencer?!\033[m')
sleep(2)
print('''\033[1mEscolha:
[1] Pedra
[2] Papel
[3] Tesoura\033[m''')
sleep(2)
jogador = int(input('\033[1;31mQual sua decisão?\033[m'))
sleep(2)
print('\033[1;37mJO\033[m')
sleep(2)
print('\033[1;37mKEN\033[m')
sleep(2)
print('\033[1;37mPÔ\033[m')
sleep(2)
Pedra = str('Pedra')
Papel = str('Papel')
Tesoura = str('Tesoura')
lista = [Pedra , Papel, Tesoura]
python = choice(lista)
if jogador == 1 and python == Tesoura or jogador == 2 and python == Pedra or jogador == 3 and python == Papel:
    print('Você venceu! Mas não vou errar novamente')
    print('Vitória! Python escolheu \033[1;32m{}\033[m'.format(python))
elif jogador == 1 and python == Papel or jogador == 2 and python == Tesoura or jogador == 3 and python == Pedra:
    print('Fraco , eu venci e posso fazer isso o dia todo')
    print('Derrota , Python escolheu:\033[1;31m{}\033[m.'.format(python))
else:
    print('Empate, tente novamente!')
    print('Python escolheu \033[1;33m{}\033[m'.format(python))
