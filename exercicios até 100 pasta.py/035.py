reta1 = int (input ('digite o valor de um reta: '))
reta2 = int (input ('digite mais um valor: '))
reta3 = int (input ('digite um ultimo valor: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print ('o valor de suas retas formam um triangulo')
else:
    print ('o valor das retas não formam um triangulo')