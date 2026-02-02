print ('para se inscrever no curso de natação eu preciso da sua idade, assim direi em que cateegoria vc está')
idade = int (input ('qual é a sua idade? '))

if idade <= 9:
    print ('vc é nivel mirim')
elif idade > 9 and idade <= 14:
    print ('vc é nivel infantil')
elif idade > 14 and idade <= 19 :
    print ('vc é junior')
elif idade == 20:
    print ('vc é senior')
else:
    print ('vc é master')