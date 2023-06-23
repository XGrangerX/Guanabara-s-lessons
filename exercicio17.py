from math import hypot
a = float(input('Qual o comprimento do cateto oposto?'))
b = float(input('Qual o comprimento do cateto adjacente?'))
c = hypot(a , b)
print('Cateto oposto {}, cateto adjacente {}, hipotenusa {:.2f}.'.format(a,b,c))
