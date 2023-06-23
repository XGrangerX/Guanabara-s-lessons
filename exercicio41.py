from datetime import date
nasc = int(input('Qual o ano de nascimento?'))
idade= date.today().year - nasc
if idade < 10:
    print('\033[34m{} anos classificação MIRIM!\033[m'.format(idade))
elif idade >=10 and idade <=14:
    print('\033[34m{} anos classificação INFANTIL!\033[m'.format(idade))
elif idade >=15 and idade <=19:
    print('\033[34m{} anos classificação JUNIOR!\033[m'.format(idade))
elif 20 <= idade <= 25:
    print('\033[34m{} anos classificação SÊNIOR!\033[m'.format(idade))
else:
    print('\033[34m{} anos classificação MASTER\033[m'.format(idade))