'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
por aluno e apresentar:
• A mensagem "Aprovado com Distinção", se a média for igual a dez.
• A mensagem "Aprovado", se a média alcançada for maior ou igual a sete, porém diferente de dez;
• A mensagem "Em exame", se a média for menor do que sete, porém maior ou igual a três;
• A mensagem "Reprovado", se a média for menor do que três;
'''

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1+n2)/2

if media == 10:
    mensagem = 'aprovado com distinção'
elif media >= 7:
    mensagem = 'aprovado'
elif media >= 3:
    mensagem = 'em exame'
else:
    mensagem = 'reprovado'

print(f'A média do aluno é igual a {media} e o aluno está {mensagem}')