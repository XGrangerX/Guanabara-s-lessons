resp = 'S'
soma = media = quant = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número?'))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
                menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('\033[31m{}\033[m valores digitados, a média dos valores é de:\033[34m{:.0f}\033[m.'.format(quant,media))
print('O maior valor foi \033[32m{}\033[m e o menor valor foi\033[33m {}\033[m.'.format(maior,menor))