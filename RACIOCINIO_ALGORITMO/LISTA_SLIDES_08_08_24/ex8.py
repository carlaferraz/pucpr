'''
Criar um programa que solicitado ao usuário as quatro notas bimestrais de um
matéria e quantas faltas este aluno teve. Informar se o aluno foi aprovado ou
reprovado, bem como o motivo. A saber:
a.A média anual é 7;
b.A disciplina possui 40 aulas;
c.O mínimo exigido é 75% de presença
'''

n1 = float(input('Digite a nota do primeiro bimestre: '))
n2 = float(input('Digite a nota do segundo bimestre: '))
n3 = float(input('Digite a nota do terceiro bimestre: '))
n4 = float(input('Por fim, digite a nota do quarto bimestre: '))
faltas = int(input('Digite o número de faltas totais do aluno: '))

media = (n1+n2+n3+n4)/4


# resposta extensa
'''
if media >= 7 and faltas<=30:
    print('O aluno está aprovado!')
elif media < 7 and faltas<=30:
    print('O aluno está reprovado por média!')
elif media >= 7 and faltas>30:
    print('O aluno está reprovado por faltas!')
else:
    print('O aluno está reprovado por falta e por média!')
'''

#respposta compacta
resultado = 'aprovado' if media>=7 else 'reprovado'
presença = 'aprovado' if faltas <= 30 else 'reprovado'


print(f'Em relação a média o aluno está {resultado}, e em relação às faltas o aluno está {presença}')

print('SITUAÇÃO FINAL: APROVADO' if resultado == 'aprovado' and presença == 'aprovado' else 'SITUAÇÃO FINAL: REPROVADO!')