from random import randint
print('='* 30)
print('{:^30}'.format('GERADOR DE JOGOS DA MEGA SENA'))
print('='* 30)
valores = []
continuar = ' '
cont = 0
while True:
    v = randint(0 , 60)
    print('Valor adicionado...')
    if v not in valores:
        valores.append(v)
        cont += 1
    else:
        print('Valor duplicado! Não sera registrado!')
    if cont ==6:
            break
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        if cont < 6:
            print('Seu jogo não está incompleto')
        break

print(f'Valores registrados: {sorted(valores)} .')
print('Fim do programa')