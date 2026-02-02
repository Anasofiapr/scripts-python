print ('joãozinho fez duas provas de matematica em 2 bimestres')

nota1 = float (input ('defina a nota de joãozinho no primeiro bimestre: '))
nota2 = float (input ('defina a nota de joãozinho no segundo bimestre: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print ('joãozinho foi reprovado.')
elif 5.0 <= media <= 6.9:
    print ('joãozinho está de recuperação.')
else:
    print ('joãozinho foi aprovado!')