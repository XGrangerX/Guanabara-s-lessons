from random import randint
itens = ('Pedra' ,'Papel','Tesoura')
Python = randint(0,2)                # 0=Pedra 1=Papel 2=Tesoura
#print('O Python escolheu {}!'.format(itens[Python])) # .format(itens[Python]) faz com que o randint
 # retorne o nome dos itens ao invés do numero do item.

print('''Suas opções
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua jogada?'))
print('-='*11)
print('O Python escolheu {}'.format(itens[Python]))
print('O Jogador escolheu {}'.format(itens[jogador]))
print('-='*11)
if Python == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('PYTHON VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif Python == 1:
    if jogador == 0:
        print('PYTHON VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif Python == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('PYTHON VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
