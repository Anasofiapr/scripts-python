frase = str (input ('digite uma frase: '))
frase = frase.lower()
frase = frase.replace(' ' , '')

if frase [::-1] == frase:
    print ('essa é uma frase polindromo!')
else:
    print ('que frase normal!')