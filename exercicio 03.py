v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segundo valor:'))
print('A soma de {} mais {} é {}!'.format(v1 , v2 , v1 + v2))

cores = {'limpa':'\033[m', 'azul':'\033[34m','amarelo':'\033[33m','pretoebranco':'\033[7;30m', 'vermelho':'\033[4;31m'}
print('A soma de {}{}{} mais {}{}{} é {}{}{}!'.format(cores['azul'],v1 ,cores['limpa'] ,cores['amarelo'] , v2 ,cores['limpa'],cores['vermelho'] ,v1 + v2,cores['limpa']))