'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida
'''

dia = int(input('Digite um dia (dd): '))
mes = int(input('Digite um mês (mm): '))
ano = int(input('Digite um ano (aaaa): '))


if mes >= 1 and mes <= 12:
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia >= 1 and dia <= 29:
                mensagem = (f'a data {dia:02d}/{mes:02d}/{ano} é válida!')
            else:
                mensagem = (f'A data {dia:02d}/{mes:02d}/{ano} é inválida! Por favor, tente novamente')
        else:
            if dia >= 1 and dia <= 28:
                mensagem = (f'a data {dia:02d}/{mes:02d}/{ano} é válida!')
            else:
                mensagem = (f'A data {dia:02d}/{mes:02d}/{ano} é inválida! Por favor, tente novamente')

        # meses com 30 dias: abr, jun, set, nov
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <=30:
            mensagem = (f'A data {dia:02d}/{mes:02d}/{ano} é válida!')
        else:
            mensagem = (f'A data {dia:02d}/{mes:02d}/{ano} é inválida! Por favor, tente novamente')

    else:
        if dia >=1 and dia <=31:
            mensagem = (f'A data {dia:02d}/{mes:02d}/{ano} é válida!')
        else:
            mensagem = (f'A data {dia:02d}/{mes:02d}/{ano} é inválida! Por favor, tente novamente')

else:
    mensagem = (f'A data {dia:02d}/{mes:02d}/{ano} é inválida! Por favor, tente novamente')


print(mensagem)
