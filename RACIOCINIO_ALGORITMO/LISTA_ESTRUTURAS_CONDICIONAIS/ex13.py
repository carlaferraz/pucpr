'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido
'''

dia = int(input('Digite um número de 1 a 7: '))


if dia > 0 and dia < 8:
    if dia == 1:
        mensagem = ('Domingo')
    elif dia == 2:
        mensagem = ('Segunda-Feira')
    elif dia == 3:
        mensagem = ('Terça-Feira')
    elif dia == 4:
        mensagem = ('Quarta-Feira')
    elif dia == 5:
        mensagem = ('Quinta-Feira')
    elif dia == 6:
        mensagem = ('Sexta-Feira')
    elif dia == 7:
        mensagem = ('Sábado') 
    print(f'o número {dia} equivale ao dia ', mensagem) 
else:
    print('Número inválido, por favor, digite outro número')