quantidade = 0
soma = 0
while True:
    numero = int (input ('digite um numero inteiro (999 pra parar): '))
    if numero == 999:
        break
    
    soma += numero
    quantidade += 1
print (f'a soma do(s) {quantidade} numero(s) sem contar a flag é: {soma}')

