numero = float (input ('digite um numero inteiro qualquer: '))
resultado = 1
contador = numero 

while contador > 1:
   resultado *= contador
   contador -= 1

print (f'o fatorial do numero {numero} é {resultado}')