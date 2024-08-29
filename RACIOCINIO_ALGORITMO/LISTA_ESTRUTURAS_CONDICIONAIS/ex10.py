'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar “M”-matutino, “V”-Vespertino ou “N”-
Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", caso não tenha sido
digitada uma letra válida
'''

turno = str(input('Olá! Qual o turno que você trabalha? M para manhã, T para tarde e N para noite '))


#resposta extensa
'''
if turno == 'M':
    print('Bom dia!')
elif turno == 'T':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Resposta inválida, por favor, digite M, T ou N para seu turno')
'''

#resposta compactada
mensagem = (
    'Bom dia!' if turno == 'M' else
    'Boa tarde!' if turno =='T' else 
    'Boa noite!' if turno == 'N' else 
    'Resposta inválida, por favor, digite M, T ou N para seu turno'
)

print(mensagem)