from random import randint
print('=='*20)
print('Vamos jogar par ou impar!'.upper())
print('=='*20)
cont=0
while True:
    valor_jogador = int(input('Digite um valor:'))
    palpite = ' '
    valor_computador = randint(0, 100)
    resultado = valor_jogador + valor_computador
    while palpite not in 'PI':
        palpite = str(input('Escolha par ou impar: [P/I]')).strip().upper()[0]
    print(f'Você jogou {valor_jogador} e o computador jogou {valor_computador} total {resultado}')
    print('Deu Par' if resultado % 2 == 0 else 'Deu impar')
    if palpite == 'P':
        if resultado % 2 == 0:
            print('Você venceu')
            cont +=1
        else:
            print('Você perdeu!')
            break
    elif palpite == 'I':
        if resultado %2 == 1:
            print('Você venceu')
            cont +=1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente')
print(f'foram {cont} vitorias seguidas')
