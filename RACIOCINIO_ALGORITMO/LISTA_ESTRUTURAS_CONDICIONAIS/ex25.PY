'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve, ao final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".
'''

print('Digite "s" para "Sim" e "n" para "Não", a fim de responder as seguintes perguntas: ')

resp = 0

a = str(input('Telefonou para a vítima?: '))
if a == 's':
    resp += 1
b = str(input('Esteve no local do crime?: '))
if b == 's':
    resp += 1
c = str(input('Mora perto da vítima?: '))
if c == 's':
    resp += 1
d = str(input('Devia para a vítima?'))
if d == 's':
    resp += 1
e = str(input('Já trabalhou com a vítima?'))
if e == 's':
    resp += 1

if resp == 2:
    classificacao = 'suspeita'
elif resp >=3 and resp <=4:
    classificacao = 'cúmplice'
elif resp == 5:
    classificacao = 'assassino'
else:
    classificacao = 'inocente'


print(f'De acordo com as respostas, o sujeito é classificado como {classificacao}')
