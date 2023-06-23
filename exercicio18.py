import math
a = float(input('Qual o ângulo?'))
seno = math.sin(math.radians(a))
print('O ãngulo de {} tem o seno de {:.2f}.'.format(a , seno))
cosseno = math.cos(math.radians(a))
print('O ãngulo de {} tem o cosseno de {:.2f}.'.format(a , cosseno))
tangente = math.tan(math.radians(a))
print('O ãngulo de {} tem a tangente de {:.2f}.'.format(a , tangente))