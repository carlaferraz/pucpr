'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
calcule a sua média, e transforme-a em Conceito. A atribuição de conceitos obedece a tabela abaixo

MÉDIA DE APROVEITAMENTO     CONCEITO
entre 9 e 10                A
entre 7.5 e 9               B
entre 6 e 7.5               C
entre 4 e 6                 D
entre 4 e 0                 E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E
'''

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2)/2

if media <= 4:
    conceito = 'E'
elif media <=6:
    conceito = 'D'
elif media <= 7.5:
    conceito = 'C'
elif media <= 9:
    conceito ='B'
else: 
    conceito = 'A'

if conceito == 'A':
    situacao = 'aprovado'
elif conceito == 'B':
    situacao = 'aprovado'
elif conceito == 'C':
    situacao = 'aprovado'
else:
    situacao = 'reprovado'



print(f'As notas do aluno foram {nota1} e {nota2}. Sua média é igual a {media:.2f} e seu conceito {conceito}. Portanto o aluno está {situacao}')


