'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada
por aluno e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c. A mensagem "Aprovado com Distinção", se a média for igual a 10
'''

n1 = float(input('Digite a nota do primeiro bimestre: '))
n2 = float(input('Digite a nota do segundo bimestre: '))
n3 = float(input('Digite a nota do terceiro bimestre: '))


media = (n1+n2+n3)/3

if media == 10:
    mensagem = 'aprovado com distinção'
elif media >= 7:
    mensagem = 'aprovado'
else:
    mensagem = 'reprovado'

print(f'A média do aluno é igual a {media} e o aluno está {mensagem}')

