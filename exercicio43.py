p = float(input('Digite o peso (Kg):'))
a = float(input('Digite a altura (m):'))
imc = p / (a**2)
if imc <= 18.5:
    max = 25 * (a**2)
    min = 18.5 * (a**2)
    print('Cuidado você está abaixo do peso! Seu IMC é de \033[31m{:.2f}\033[m.'.format(imc))
    print('Seu peso ideal está entre\033[32m {:.2f}\033[m e \033[32m{:.2f} quilos\033[m.'.format(min, max))
elif 18.5 <= imc < 25:
    max = 25 * (a ** 2)
    min = 18.5 * (a ** 2)
    print('Muito bem peso ideal! Seu IMC é de \033[34m{:.2f}\033[m.'.format(imc))
    print('Seu peso ideal está entre\033[32m {:.2f}\033[m e \033[32m{:.2f} quilos\033[m.'.format(min, max))
elif 25 <= imc < 30:
    max = 25 * (a ** 2)
    min = 18.5 * (a ** 2)
    print('Cuidado você possui sobrepeso! Seu IMC é de \033[33m{:.2f}\033[m.'.format(imc))
    print('Seu peso ideal está entre\033[32m {:.2f}\033[m e \033[32m{:.2f} quilos\033[m.'.format(min, max))
elif 30 <= imc < 40:
    max = 25 * (a ** 2)
    min = 18.5 * (a ** 2)
    print('Cuidado você possui \033[4;31mOBESIDADE!\033[m Seu IMC é de \033[31m{:.2f}\033[m.'.format(imc))
    print('Seu peso ideal está entre\033[32m {:.2f}\033[m e \033[32m{:.2f} quilos\033[m.'.format(min, max))
else:
    max = 25 * (a ** 2)
    min = 18.5 * (a ** 2)
    print('Cuidado você possui \033[4;31mOBESIDADE MÓRBIDA!\033[m Seu IMC é de \033[31m{:.2f}\033[m.'.format(imc))
    print('Seu peso ideal está entre\033[32m {:.2f}\033[m e \033[32m{:.2f} quilos\033[m.'.format(min, max))
