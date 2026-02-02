import logging
from math import inf

logging.basicConfig(level=logging.ERROR)

mais_barato = (inf)
nome_barato = ''
total = 0
maior_que_mil = 0

while True:
    print ("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ANA'S ATACADÃO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
    
    produto = input ('nome do produto: ')
    valor = int (input ('valor do produto: '))
    
    total += valor
    valor2 = valor
   
    if valor > 1000:
        maior_que_mil += 1
    
    if valor < mais_barato:
        mais_barato = valor2
        nome_barato = produto
    
    continuar = str (input ('Deseja continuar? [N/S] ')).upper()
    logging.info(f"{continuar=} | {mais_barato=}")
    
    if continuar == 'N':
        break
print (f"""O seu gasto total foi de: {total}
temos {maior_que_mil} produtos que custam mais que mil
O produto mais barato é: {nome_barato}""")