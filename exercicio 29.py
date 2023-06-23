from time import sleep
from random import randint
print('Carro se aproximando do radar...')
sleep(2)
print('Registrando velocidade...')
sleep(2)
vel=randint(77,90)
print('{}km/h'.format(vel))
m= (vel-80)*7
if vel < 80:
    print('Direção segura sem multas!')
if vel >= 81:
    print('Muito veloz , sua multa será de R${:.2f}!'.format(m))
