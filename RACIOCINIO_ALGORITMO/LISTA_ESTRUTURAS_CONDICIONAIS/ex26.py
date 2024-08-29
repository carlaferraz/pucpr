'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
• até 20 litros, desconto de 0,3 centavos por litro;
• acima de 20 litros, desconto de 0,5 centavos por litro;
Gasolina:
• até 20 litros, desconto de 4% por litro
• acima de 20 litros, desconto de 6% por litro
Escreva um programa que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-
álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$
6,60 e o preço do litro do álcool é R$ 4,60
'''




litro = float(input('Digite o número de litros vendidos: '))
combustivel = input('Digite "A" para "álcool" e "G" para "gasolina" para informar o tipo de combustível): ')


alcool=4.60
gasolina=6.60
valor_desconto=0

if combustivel == 'A':
    if litro <= 20:
        desconto = 0.30
    else:
        desconto = 0.50
    valor = litro * alcool
    valor_desconto = valor - (desconto*litro/100)
    
elif combustivel == 'G':
    if litro <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor = litro * gasolina
    valor_desconto = valor - (valor*desconto)

else:
    print('Tipo de combustível inválido, por favor, tente novamente')
    valor_desconto = 0


if valor_desconto > 0:
    print(f'Valor total a pagar é de R$ {valor_desconto:.2f}')
