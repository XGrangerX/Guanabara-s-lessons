print('Gerador de PA')
print('-=' * 10)
p = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
termo = p
cont = 1
while cont <= 10:
    print('{}¬'.format(termo), end='')
    termo += r
    cont += 1
print('FIM')
