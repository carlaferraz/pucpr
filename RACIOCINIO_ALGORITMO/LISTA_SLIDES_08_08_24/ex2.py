'''
Elaborar um algoritmo que solicita ao usuário seu ano de nascimento e calcula sua idade com relação ao ano corrente. Em seguida pergunte se o usuário já fez aniversário neste ano. Se a resposta for sim, mostre a mensagem “Que pena!”, caso contrário, mostre a mensagem “Onde será a festa?
'''

ano_nasc = int(input('Qual o ano que você nasceu? '))

fez_aniver = str(input('Responda com SIM se você já fez aniversário esse ano, e com NÃO se ainda não fez '))

idade = 2024 - ano_nasc


#resposta extensa
'''
if fez_aniver == 'SIM':
    print(f'Que pena! Então você já fez aniversário e possui {idade} anos')
elif fez_aniver == 'NÃO':
    idade -= 1
    print(f'Então você ainda tem {idade} anos! Onde será a festa do seu aniversário de {idade + 1} anos?')
else:
    print('Por favor, tente novamente respondendo SIM ou NÃO')
'''

#resposta compactada
mensagem = (
    f'Que pena! Então você já fez aniversário e possui {idade} anos' if fez_aniver == 'SIM' else
    f'Então você ainda tem {idade} anos! Onde será a festa do seu aniversário de {idade + 1} anos?' if fez_aniver == 'NÃO' else
    'Por favor, tente novamente respondendo SIM ou NÃO'
)

print(mensagem)