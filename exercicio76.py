list = ('pão', 0.25 ,
        'leite',3.50,
        'manteiga', 4.69,
        'café', 5.50,
        'ovos',8.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}') # :^40 serve pra preencher 40 caracteres centralizando
print('-'*40)
for pos in range(0 , len(list)): # para cada item (pos) no range de len de list, ou seja a quantidade de elementos em lista
    if pos % 2 == 0:            #se a posição do elemento for par ele da print em produto
        print(f'{list[pos]:.<30}', end='') # :.<30 alinha o texto a esquesrda preenchando 30 carateres com ponto
    else:                       #senão ( se a posição for impar) ele da print no preço
        print(f'R${list[pos]:>7.2f}')  # :>7.2f alinha o texto a direita preenchando 7 carateres com espaço e
                                        # exibe 2 casa decimais de preço
print('-'*40)