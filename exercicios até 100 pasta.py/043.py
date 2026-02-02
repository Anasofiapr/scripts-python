altura = float (input ('digite sua altura: '))
peso = float (input ('digite seu peso: '))

imc = peso / altura  ** 2

print (f'Seu IMC (indice de massa corporea): {imc :.2f}')

if imc < 18.5:
    print ('abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print ('Peso ideal')
elif imc > 25 and imc <= 30:
    print ('sobrepeso')
elif imc > 30 and imc <= 40:
    print ('obesidade')
else:
    print ('obesidade mórbida')