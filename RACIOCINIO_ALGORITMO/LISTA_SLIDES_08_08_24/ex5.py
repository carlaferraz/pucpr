'''
Criar um programa que pergunte ao usuário em que turno trabalha. Formato da entrada: “M” - Manhã, “T” - Tarde ou “ N” - Noite. Mostre a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!" conforme o turno informado, ou "Valor Inválido!", para outras entradas
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

