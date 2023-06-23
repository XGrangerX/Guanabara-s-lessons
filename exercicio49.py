u = int(input('Deseja saber a tabuada de qual numero?'))
for c in range(1,11):
    print('\033[4;34m{}\033[m x \033[4;31m{:2}\033[m =\033[4;32m {:2}\033[m.'.format(u,c,u*c))
