feirinha = ['maçã','banana','tomate','morango','pera','kiwi','coco','abacaxi','melancia','melão','graviola','abacate']

print ('a feirinha de frutas está numa promoção de 7 reais cada fruta')
item = input ('pegue um item da feirinha de frutas: ')
item = item.lower()

print ('as formas de pagamento são: cheque, dinheiro, a vista no cartão, duas vezes no cartão e três vezes no cartão')
cheque_dinheiro = (7 * 10) / 100
vista_cartao = (7 * 5) / 100
duas_cartao = 07.00
juros = 7 - (7 * 20) / 100 
tres_cartao =  7 + juros

if item in feirinha:
    print (f'pegou o item {item}')
    forma_de_pagamento = input ('qual seria a forma de pagamento? ')
    forma_de_pagamento = forma_de_pagamento.lower()
    
    if forma_de_pagamento == 'cheque':
        print (f'vc recebeu 10% de desconto! valor total: { 7 - cheque_dinheiro}')
    elif forma_de_pagamento == 'dinheiro':
        print (f'vc recebeu 10% de desconto! valor total: { 7 - cheque_dinheiro}')
    elif forma_de_pagamento == 'a vista no cartão':
        print (f'você recebeu 5% de desconto! valor total: {7 - vista_cartao}')
    elif forma_de_pagamento == 'duas vezes no cartão':
        print (f'o valor total a pagar é de: 07,00 reais')
    elif forma_de_pagamento == 'três vezes no cartão': 
        print (f'Seu item veio com juros, valor total: {tres_cartao}')
else:
    print ('nao tem esse item na feirinha tente novamente')