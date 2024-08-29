'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de
centenas, dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e",
da vírgula entre outros. Exemplo:
• 326 = 3 centenas, 2 dezenas e 6 unidades
• 12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''


num = int(input('Digite um número de 0 a 999: '))


if 0 <= num < 1000:
    unidade = num % 10
    dezena = (num // 10) % 10
    centena = num // 100

    if unidade > 1:
        mensagem_uni = (f'{unidade} unidades')
    elif unidade == 1:
        mensagem_uni = (f'1 unidade')
    else:
        mensagem_uni = ''

    if dezena > 1:
        mensagem_dez = (f'{dezena} dezenas')
    elif dezena == 1:
        mensagem_dez = (f'1 dezena')
    else:
        mensagem_dez = ''
    
    if centena > 1:
        mensagem_cen = (f'{centena} centenas')
    elif centena == 1:
        mensagem_cen = (f'1 centena')
    else:
        mensagem_cen = ''



    if unidade >= 1 and dezena >= 1 and centena >=1:
        mensagem = f'O número {num} possui {mensagem_cen}, {mensagem_dez} e {mensagem_uni}'
    elif unidade == 0 and dezena >=1 and centena >=1:
        mensagem = f'O número {num} possui {mensagem_cen} e {mensagem_dez}'
    elif unidade >=1 and dezena == 0 and centena >=1:
        mensagem = f'O número {num} possui {mensagem_cen} e {mensagem_uni}'
    elif unidade >=1 and dezena >=1 and centena == 0:
        mensagem = f'O número {num} possui {mensagem_dez} e {mensagem_uni}'
    elif unidade == 0 and dezena == 0 and centena >=1:
        mensagem = f'O número {num} possui {mensagem_cen}'
    elif unidade == 0 and dezena >=1 and centena ==0:
        mensagem = f'O número {num} possui {mensagem_dez}'
    elif unidade >=1 and dezena == 0 and centena ==0:
        mensagem = f'O número {num} possui {mensagem_uni}'
    else:
        mensagem = f'O número {num} não possui centenas, dezenas ou unidades'

    print(mensagem)

else:
    print('Número inválido, por favor, tente novamente.')
