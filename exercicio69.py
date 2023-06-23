maior_de_18 = homem = pessoas =mulher =0
while True:
    print('='*30)
    print('Cadastre uma pessoa:')
    print('=' * 30)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    pessoas += 1
    if  idade >= 18:
        maior_de_18 += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade <= 20:
        mulher += 1
    if continuar in 'Nn':
        break
print(f'Foram cadastrados {pessoas} pessoas sendo: {maior_de_18} pessoas maiores de 18, {homem} homens, e {mulher} mulheres abaixo de 20 anos')


