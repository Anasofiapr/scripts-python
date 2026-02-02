print ('-' *100)
print ('sequencia de fibonacci')
print ('-' *100)

numero = int (input ('quantos termos vc quer que apareça? '))
termo1 = 0
termo2 = 1

print (f'=> {termo1} => {termo2}', end=' ') 
count = 3
while count <= numero: 
    termo3 = termo1 + termo2
    print (f'=> {termo3}', end=' ')
    count  += 1
    termo1 = termo2
    termo2 = termo3
print ('=> fim')