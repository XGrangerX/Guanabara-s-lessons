a = int(input('Digite um valor:'))
c=str(input('Deseja convertelo em: \n 1-Binario\n 2-Octal\n 3-hexadecimal\n'
            'Sua escolha:'))
if c =='1':
    print(bin(a)[2:])
elif c =='2':
    print(oct(a)[2:])
elif c == '3':
    print(hex(a)[2:])
else:
    print('Error: conversion not found! ')

# '0b = binario' , '0o = octal' , '0x = hexadecimal'

# [2:] mostra os cacteres a partir da segunda casa ate a ultima