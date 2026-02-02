salario = float (input('vc é um funcionario de uma empresa, qual é o seu salário? '))
 
if salario > 1250.00:
   calculo = (salario * 10) / 100
   aumento = salario + calculo 
else: 
   calculo2 = (salario * 15) / 100
   aumento2 = salario + calculo2
   
if salario > 1250.00:
   print (f'você recebeu um aumento de 10%! Se salario agora é de: {aumento}')
else:
   print ('você recebeu um aumento de 15%! Se salario agora é de: {:.2f}'.format (aumento2))
