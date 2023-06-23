n = str(input('Qual seu nome completo?')).strip()
nome = n.split() #split gera uma lista com os pedaços do nome
print('Muito prazer em te conhecer')
print('Seu prieiro nome é {}.'.format(nome[0]))
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1])) #len conta as posiçoes do nome por palavra