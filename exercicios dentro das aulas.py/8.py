from math import sqrt,ceil

num = int(input('digite um numero'))
raiz = sqrt(num)

if raiz.is_integer():
    print (f'a raiz de {num} é igual a {raiz:.0f}')
else: 
    print('a raiz de {} é aproximadamente {:.2f}'.format (num, raiz))
