from random import shuffle
aluno1 = str (input ('você é um professor, digite o nome de um dos seus alunos'))
aluno2 = str (input ('digite o nome de mais um aluno'))
aluno3 = str (input ('digite o nome de outro aluno'))
aluno4 = str (input ('digite mais um nome de aluno'))

print ('agora esses alunos tem um trabalho na escola, eles precisam apresentar, deixa que eu faça a ordem de apresentação!')
lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print ('ordem da apresentação:')
print (lista)
