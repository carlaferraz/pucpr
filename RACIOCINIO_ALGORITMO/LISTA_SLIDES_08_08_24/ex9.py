'''
Criar um programa que simule um caixa eletrônico. O programa deverá perguntar o valor do saque e depois informar quantas e quais notas serão fornecidas, a saber:
a.Moedas disponíveis: 1 Real
b.Notas disponíveis: 2, 5, 10, 50, 100 e 200 Reais;
c.Valor mínimo de saque: R$ 10,00 Reais;
d.Valor máximo de saque: R$ 6.000,00 Reais.
'''

valor = float(input('Qual o valor do saque? Mínimo: RS10,00 e máximo: R$6000,00: '))

if valor >= 10 and valor <= 6000:

    d = cem = cinq = dez = cin = dois = um = 0

    d = valor // 200
    rd = valor % 200
    if rd / 100 > 0:
        cem = rd // 100
        rcem = rd % 100
        if rcem / 50 > 0:
            cinq = rcem // 50
            rcinq = rcem % 50
            if rcinq / 10 > 0:
                dez = rcinq // 10
                rdez = rcinq % 10
                if rdez / 5 > 0:
                    cin = rdez // 5
                    rcin = rdez % 5
                    if rcin / 2 > 0:
                        dois = rcin // 2
                        rdois = rcin % 2
                        if rdois / 1 > 0:
                            um = rdois // 1
                            rum = rdois % 1


    mensagem = (
        f'''
        NOTAS DE DUZENTOS: {d}'
        NOTAS DE CEM: {cem}
        NOTAS DE CINQUENTA: {cinq}
        NOTAS DE DEZ: {dez}
        NOTAS DE CINCO: {cin}
        NOTAS DE DOIS: {dois}
        MOEDAS DE UM: {um}'''
    )
    print(mensagem)
                    
else:
    print ('Valor inválido! Digite outro valor')