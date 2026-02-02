num1 = int (input ('digite um numero inteiro qualquer: '))
num2 = int (input ('digite outro numero inteiro qualquer: '))

maior_numero = num1
menor_numero = num2

if num2 > num1:
    print ('o primeiro numero é o menor')
    print ('o segundo numero é o maior')
elif num1 > num2:
   print ('o primeiro numero é o maior')
   print ('o segundo numero é o menor')
elif num2 == num1:
    print ('os dois numeros tem valores iguais')