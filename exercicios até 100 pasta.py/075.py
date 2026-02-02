numero1 = int (input ('Digite um numero: '))
numero2 = int (input ('Digite outro numero: '))
numero3 = int (input ('Digite mais um numero: '))
numero4 = int (input ('Digite mais um numero pela ultima vez: '))

numeros = (numero1 , numero2 , numero3 , numero4)

print (f'O numero nove aparece {numeros.count(9)} vezes na sequência')

if 3 in numeros:
    print (f'O primeiro numero três está na {numeros.index(3)+1}ª posição')
else:
    print ('não tem um numero três na sequência')

pares = ()

for n in numeros: 
    if n % 2 == 0:
        pares += (n,)

print (pares)