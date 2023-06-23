a= str(input('Digite seu nome:')).strip()  # .strip elimina espaços antes e depois da cadeia de caracteres
print(a.upper())
print(a.lower())
print(len(a)-a.count(' ')) #.coun('espaço') elimina da contagem os espaços entre as palavras
print('Seu primeiro nome tem {} letras.'.format(a.find(' '))) # .find encontra o primeiro espaço do nome e considera a quantidade de caracteres anteriores ao espaço
separa = a.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))