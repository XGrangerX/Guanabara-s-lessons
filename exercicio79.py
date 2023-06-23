valores = []
continuar = ' '
while True:
    v = int(input('Digite um valor: '))
    print('Valor adicionado...')
    if v not in valores:
        valores.append(v)
    else:
        print('Valor duplicado! Não sera registrado!')
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
print(f'Valores registrados: {sorted(valores)} .')
print('Fim do programa')
