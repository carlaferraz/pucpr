'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O
valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de
notas existentes na máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma
nota de 5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
quatro notas de 10, uma nota de 5 e quatro notas de 1
'''

valor = int(input('Qual o valor do saque? Mínimo: RS10,00 e máximo: R$600,00: '))

if valor >= 10 and valor <= 600:

    cem = cinq = dez = cin = dois = um = 0

    cem = valor // 100
    valor %= 100

    cinq = valor // 50
    valor %= 50

    dez = valor // 10
    valor %= 10

    cin = valor // 5
    valor %= 5

    um = valor // 1
                        

    mensagem = (
    f'''
    NOTAS DE CEM: {cem}
    NOTAS DE CINQUENTA: {cinq}
    NOTAS DE DEZ: {dez}
    NOTAS DE CINCO: {cin}
    MOEDAS DE UM: {um}
'''
    )
    print(mensagem)
                    
else:
    print ('Valor inválido! Digite outro valor')