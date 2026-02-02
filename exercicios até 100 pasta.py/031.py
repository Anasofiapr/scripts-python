print ('você fará uma viagem')
duracao = float (input('digite quantos km/h essa viagem irá durar: '))
valor_200 = duracao * 0.50
valor_mais = duracao * 0.45

if duracao <= 200:
    print (f'o valor da viagem de {duracao} km/h é de: {valor_200}')
else:
    print (f'o valor da viagem de {duracao} km/h é de: {valor_mais}')