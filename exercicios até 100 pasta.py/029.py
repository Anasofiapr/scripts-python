km = int (input('vc está andando de carro, defina a velocidade do seu carro: '))
multa = 7 * (km - 80)

if km > 80:
    print (f'você ultrapassou o limite de velocidade, sua multa é de: {multa}')
else:
    print ('você está dentro do limite de velocidade! está liberado para prosseguir!')