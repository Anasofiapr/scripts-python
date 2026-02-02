import random
import emoji

aluno1 = input ('você é um professor, digite o nome de um dos seus alunos')
aluno2 = input ('digite o nome de mais um aluno')
aluno3 = input ('digite o nome de outro aluno')
aluno4 = input ('digite mais um nome de aluno')

alunos = aluno1,aluno2,aluno3,aluno4
aluno_que_vai_apagar_o_quadro = random.choice (alunos)


print ('esses quatro alunos estão disputando para apagar o quadro, deixe que o python resolva seus problemas')
print (emoji.emojize (f'pronto! o aluno {aluno_que_vai_apagar_o_quadro} irá apagar o quadro :beaming_face_with_smiling_eyes:'))
