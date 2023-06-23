from random import randint
comp = randint(0,10)
print('Descubra o número escolhido entre 0 e 10.')
print('Consegue advinhar qual foi?')
acertou=False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpite += 1
    if jogador == comp:
        acertou= True
    else:
        if jogador < comp:
            print('Mais...  o número escolhido eh maior!')
        elif jogador > comp:
            print('Menos... o número escolhido é menor')

print('Acertou com {} tentivas'.format(palpite))