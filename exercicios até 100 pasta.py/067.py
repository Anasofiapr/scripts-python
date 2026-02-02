
while True:
    numero = int (input ('digite um numero para a tabuada (um numero negativo para parar): '))
    contador = 0
    if numero < 0:
        break

    for oi in range (11):
        print (f'{numero} X {contador} = {numero * contador}')
        contador += 1
print ('PROGRAMA TABUADA ENCERRADO! volte sempre.')
