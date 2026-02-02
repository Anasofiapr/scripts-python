num1 = float (input ('digite um numero aleatório: '))
num2 = float (input ('digite outro numero aleatório: '))

print ('o que vc deseja fazer com esses numeros???')
print ("""1- Somar
2- Multiplicar
3- Maior
4- Novos numeros
5- Sair do programa""")

comando = int (input ('o que vc deseja?? '))

while comando != 5:
    if comando == 1:
        soma = num1 + num2
        print (f'a soma entre eles é: {soma}')
        comando = int (input ('deseja mais algo? '))
    if comando == 2:
        veses = num1 * num2
        print (f'a multiplicação entre eles é: {veses}')
        comando = int (input ('deseja mais algo? '))
    if comando == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print (f'o maior numero é: {maior}')
        comando = int (input ('deseja mais algo? '))
    if comando == 4:
        num1 = float (input ('digite um novo numero: '))
        num2 = float (input ('digite um segundo novo numero: '))
        print (f'seus novos numeros são {num1,num2}')
        comando = int (input ('deseja mais algo? '))

if comando == 5:
    print ("""salvando suas respostas...
saindo do menu...""")