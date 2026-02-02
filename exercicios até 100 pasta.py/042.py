reta1 = int (input ('digite o valor de um reta: '))
reta2 = int (input ('digite mais um valor: '))
reta3 = int (input ('digite um ultimo valor: '))

if (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta3 + reta1 > reta2):
    print ('o valor de suas retas formam um triangulo')
    
    if reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print ('e esse triangulo é um triangulo isóceles')
    elif reta1 == reta2 == reta3:
        print ('e esse triangulo é um triangulo equilatero')
    else: 
        print ('e é um triangulo escaleno')
else: 
    print ('esssas retas nao podem formar um triangulo')