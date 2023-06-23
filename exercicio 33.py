a = int(input('Digite o primeiro valor...'))
b = int(input('Agora digite o segundo valor...'))
c = int(input('O ultimo valor...'))
menor = a
maior = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor é {} e o menor valor é {}.'.format(maior, menor))
