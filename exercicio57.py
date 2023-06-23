s =str(input('Digite o sexo da pessoa: ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dado inválido, Digite o sexo da pessoa: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!.'.format(s))
