from random import randint
numero_aleatorio = randint(1,5)

print ('vamos jogar um jogo, pensei em um numero, tente adivinha-lo, você tem duas chances')
numero_acha = int (input('digite um numero de 1 á 5 que você acha que eu pensei: '))
 
if numero_acha == numero_aleatorio:
    print ('Parabéns você acertou! você é muito bom nisso!')
else:
    print ('Você errou! tente novamente!')
    numero_acha2 = int (input('sua ultima chance! digite um numero: '))

if numero_acha2 == numero_aleatorio:
    print ('Parabéns você acertou!')
else:
    print ('você errou! mt ruim kkkk, reinicie o game e tente novamente!')