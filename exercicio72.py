extensos = ('zero','um','dois','tres','quatro','cinco','seis',
            'sete','oito','nove','dez','onze','doze','treze','catorze'
            ,'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
user = 0
while True:
    while True:
        user=int(input('Digite um numero entre 0 e 20:'))
        continuar= ' '
        if 0 <= user <=20:
            break
        print('Tente novamente. ',end='')
    print(f'Você digitou o numero {extensos[user]}')
    while continuar not in 'SN':
        continuar = str(input('Deseja contimuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('POGRAMINHA ENCERREDIS')
