print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Seguimento a:'))
r2 = float(input('Seguimento b:'))
r3 = float(input('Seguimento c:'))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')