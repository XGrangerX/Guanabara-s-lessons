a = input('Digite algo:')
print('O tipo primitivo desse é', type(a))
print('Só tem espaços?' , a.isspace())
print('É u número?', a.isnumeric())
print('È alfabetico', a.isalpha())
print('È alfanumerico?', a.isalnum())
print('Está em maiusculas?', a.isupper())
print('Está em minusculas?', a.islower())
print('Está capitalizada?', a.istitle())
if a.isnumeric():
    print('Pago')