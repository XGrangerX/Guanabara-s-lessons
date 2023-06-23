from datetime import date
nasc = int(input('Qual o ano de nascimento?'))
idade= date.today().year - nasc
ult = idade -18
falta= 18-idade
print(idade)
if idade == 18:
    print('Voce tem \033[31m{} anos\033[m, hora de se alistar!'.format(idade))
elif idade > 18:
    print('Voce tem \033[34m{} anos\033[m, prazo de alistamento ultrapassado em \033[31m{} ano(s) \033[m!'
          .format(idade,ult))
    print('Você deveria ter se  alistado em\033[31m {}\033[m!'.format(date.today().year - ult))
else:
    print('Voce tem \033[34m{} anos\033[m, deverá se alistar em \033[31m{} ano(s) \033[m!'.format(idade,falta))
    print('Você deverá se alistar em {}!'.format(date.today().year + falta))