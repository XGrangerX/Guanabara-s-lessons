frase = ('Kakashi',
            'Hashirama',
            'Tobirama',
            'Tsunade',
            'Naruto',
            'Minato')
for palavra in frase:
    print(f'\nNa palvra {palavra.upper()} temos ',end='')
    for letra in palavra:
       if letra.lower() in 'aeiou':
           print(letra,end='')