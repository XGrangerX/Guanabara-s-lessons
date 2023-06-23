n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
if media < 5:
    print('Média {:.2f} \033[4;31m REPROVADO!\033[m'.format(media))
elif 6.99 > media > 4.99:
    print('Média {:.2f} \033[4;33m RECUPERAÇÃO!\033[m'.format(media))
else:
    print('Média {:.2f} \033[4;32m APROVADO!\033[m'.format(media))