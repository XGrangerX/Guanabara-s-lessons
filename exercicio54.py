from datetime import date
maiores = 0
menores = 0
cont =0
for c in range(1 , 8):
    nasc = int(input('Informe o ano de nascimento da {}ª pessoa:'.format(c)))
    idade = date.today().year - nasc
    cont += 1
    list = [nasc]
    if idade <= 17:
        menores += 1
    else:
        maiores += 1
print('Com total de {} participantes'.format(cont))
print('Tivemos {} pessoas menor de idade!'.format(menores))
print('Tivemos {} pessoas maiores de idade'.format(maiores))
