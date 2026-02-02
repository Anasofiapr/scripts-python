num1 = int (input('digite um numero: '))
num2 = int (input('digite um numero: '))
num3 = int (input('digite um numero: '))

maior_numero = num1
menor_numero = num2

if num3 > maior_numero:
        maior_numero = num3 
if num2 > maior_numero:
        maior_numero = num2

if num1 < menor_numero:
        menor_numero = num1
if num3 < menor_numero:
        menor_numero = num3

print ('         ')
print (f"""o maior numero é: {maior_numero}
o menor numero é: {menor_numero}""")
