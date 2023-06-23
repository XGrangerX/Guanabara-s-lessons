from random import choice
a = input('Primeiro aluno:')
b = input('Segundo aluno:')
c = input('Terceiro aluno:')
d = input('Quarto aluno:')
lista = [a , b , c, d]
escolhido = choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))