valores = []
maior = menor = 0
for cont in range(0 , 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}:')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print(f'O maior numero foi {maior} aparecendo nas posições:', end='')
for i , v in enumerate(valores): # para cada indice e valor in enumerar lista de valores
    if v == maior: #se valor for = a maior
        print(f' {i}...',end='') # mostre indice
print(f'\nO menor numero foi {menor} aparecendo nas posições:',end='')
for i , v in enumerate(valores): # para cada indice e valor in enumerar lista de valores
    if v == menor: #se valor for = a menor
        print(f' {i}...',end='') # # mostre indice