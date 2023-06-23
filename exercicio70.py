print('='*30)
print('LOJA SUPER BARATÃO')
print('='*30)
barato = ' '
tot_prod = mais_1000 = totcompra = menor = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto'))
    continuar=' '
    tot_prod += 1
    totcompra += preco
    while continuar not in 'SN':
        continuar = str(input('Deseja contimuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
    if tot_prod == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        mais_1000 += 1

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'Total de produtos: {tot_prod}')
print(f'Total da compra {totcompra}')
print(f'{mais_1000} produtos custam mais de R$1000,00')
print(f'O produto mais barato foi {barato} custando {menor:.2f}!')
