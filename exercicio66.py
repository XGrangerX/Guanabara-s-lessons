n = cont = soma = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados\033[34m {cont}\033[m valores, e a soma deles é igual a \033[34m{soma}\033[m')
