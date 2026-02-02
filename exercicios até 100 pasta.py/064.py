print ('digite 999 caso queira parar o programa')

numero = 0 
count = 0  - 1
soma = 0

while numero != 999:
    numero = float (input ('digite um numero qualquer'))
    soma += numero
    count += 1
soma -= 999
media = soma / count

print (f'vc finalizou o programa! vc digitou {count} numero(s), a soma de todos eles foi de = {soma} e a média de = {media}')

