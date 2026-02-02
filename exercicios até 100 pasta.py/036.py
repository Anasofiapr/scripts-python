print ('vc quer comprar uma casa com um emprestimo')

valor_casa = float (input ('qual é o valor da casa? '))
salario = float (input ('qual é o valor do seu salário? '))
prazo = int (input ('em quantos anos vc irá pagar? '))

prazo_em_meses = prazo * 12
prestação_mensal = valor_casa / prazo_em_meses
limite = (salario * 30) /100

if prestação_mensal > limite:
    print ('empréstimo negado')
else:
    print ('emprétimo aceito')
