num = (int(input('Digite um numero: ')),
int(input('Digite outro numero: ')),int(input('Digite mais um numero: ')),
int(input('Digite o ultimo numero: ')))
print(f'Os valores digitados foram {num}')
if 9 in num:
    print(f'O numero nove aparece {num.count(9)} vezes')
else:
    print('O numero 9 não foi digitado')
if 3 in num:
    print(f'O numero 3 aparece na {num.index(3)+1}ª posição')
else:
    print('O númro três não foi digitado!')
print(f'Os valores pares foram ',end='')
for n in num:
    if n %2 == 0:
        print(n,end=' ')
