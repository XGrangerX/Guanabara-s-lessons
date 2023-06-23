from random import randint
valores = (randint(1 , 10),randint(1 , 10),randint(1 , 10),
     randint(1 , 10),randint(1 , 10),)
print('Os valores sorteados foram: ', end='')
for cadavalor in valores:
    print(f'{cadavalor} ', end='')
print(f'\nO maior numero foi {max(valores)}')
print(f'O menor numero foi {min(valores)}')