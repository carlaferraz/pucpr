'''
Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.
'''

pontos = int(input('Qual a quantidade mínima de pontos para vencer o jogo?: '))



pontos_ganhos_user_1 = 0
pontos_ganhos_user_2 = 0

while pontos_ganhos_user_1 < pontos and pontos_ganhos_user_2 < pontos:

    escolha_user_1 = (str(input('Escolha "pe" para PEDRA, "pa" para PAPEL e "te" para TESOURA: ')))

    escolha_user_2 = (str(input('Escolha "pe" para PEDRA, "pa" para PAPEL e "te" para TESOURA: ')))


    if escolha_user_1 == 'pe':
        if escolha_user_2 == 'pe':
            mensagem = 'empate'
        elif escolha_user_2 == 'pa':
            pontos_ganhos_user_2 += 1
            mensagem ='Usuário 2 ganhou'
        else:
            pontos_ganhos_user_1 += 1
            mensagem = 'Usuário 1 ganhou'

    elif escolha_user_1 == 'pa':
        if escolha_user_2 == 'pe':
            pontos_ganhos_user_1 += 1
            mensagem = 'Usuário 1 ganhou'
        elif escolha_user_2 == 'pa':
            mensagem ='empate'
        else:
            pontos_ganhos_user_2 += 1
            mensagem = 'Usuário 2 ganhou'

    elif escolha_user_1 == 'te':
        if escolha_user_2 == 'pe':
            pontos_ganhos_user_2 += 1
            mensagem = 'Usuário 2 ganhou'
        elif escolha_user_2 == 'pa':
            pontos_ganhos_user_1 += 1
            mensagem ='Usuário 1 ganhou'
        else:
            mensagem = 'empate'

    print(f'''
PONTOS DO USUÁRIO 1: {pontos_ganhos_user_1}
PONTOS DO USUÁRIO 2: {pontos_ganhos_user_2}
''')
    

if pontos_ganhos_user_1 > pontos_ganhos_user_2:
    print('USUÁRIO 1 VENCEU')
else:
    print('USUÁRIO 2 VENCEU')
