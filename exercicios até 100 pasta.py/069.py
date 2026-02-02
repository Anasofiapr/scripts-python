mulheres_menores_de_idade = int ()
mais_de_dezoito = int ()
homens = int ()

while True:
    print (""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                CADASTRE UMA PESSOA"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """)
    
    idade = int (input ('qual é a idade? '))
    sexo = ' '
    
    while sexo not in 'MF':
        sexo = input ('qual é o sexo? [F/M] ').strip().upper()[0]
    
    if sexo == 'f' and idade < 20:
        mulheres_menores_de_idade += 1
    
    elif sexo == 'm':
        homens += 1

    if idade > 18:
        mais_de_dezoito += 1
   
    continua = ' '
    while continua not in 'SN':
         continua = input ('deseja continuar? [S/N] ').strip().upper()[0]
    if continua == 'N':
        break
print (f"""o número de mulheres com menos de 20 anos foi de: {mulheres_menores_de_idade}
O número de homens foi de: {homens}
O número de pessoas com mais de 18 anos foi de: {mais_de_dezoito}""")