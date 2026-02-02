numeros_tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze' , 'doze' , 'treze' , 'quatorze' , 'quinze' , 'dezesseis' , 'dezessete' , 'dezoito' , 'dezenove' , 'vinte')

numero_da_pessoa = int (input ('digite um numero de 0 á 20: '))
while numero_da_pessoa < 0 or numero_da_pessoa > 20:
    numero_da_pessoa = int (input ('tente novamente com um numero de 0 á 20: '))

print (f'você digitou o número: {numeros_tupla[numero_da_pessoa]}')

#de primeira!!!!!!