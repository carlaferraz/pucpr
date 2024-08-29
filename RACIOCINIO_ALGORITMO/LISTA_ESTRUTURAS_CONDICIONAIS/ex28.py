'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira
                ATÉ 5 KG                ACIMA DE 5 KG
FILÉ DUPLO      R$ 49,90 POR KG         R$ 45,80 POR KG
ALCATRA         R$ 45,90 POR KG         R$ 43,80 POR KG
PICANHA         R$ 56,90 POR KG         R$ 52,80 POR KG

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não
há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
pelo cliente e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo
de pagamento, valor do desconto e valor a pagar.
'''


p_fila5 = 49.90
p_fila6 = 45.80
p_alc5 = 45.90
p_alc6 = 43.80
p_pic5 = 56.90
p_pic6 = 52.80


tp_carne = input('Digite o tipo de carne OPÇÕES: filé duplo, alcatra, picanha: ')
kg = float(input('Digite a quantidade de carne em kg: '))
pgto = input('Digite se o pagamento é em cartão "C" ou à vista "V": ')


p_kg = 0
desc = 0


if tp_carne == 'filé duplo':
    if kg <= 5:
        p_kg = p_fila5
    else:
        p_kg = p_fila6
elif tp_carne == 'alcatra':
    if kg <= 5:
        p_kg = p_alc5
    else:
        p_kg = p_alc6
elif tp_carne == 'picanha':
    if kg <= 5:
        p_kg = p_pic5
    else:
        p_kg = p_pic6
else:
    print('Tipo de carne inválido. Por favor, tente novamente')


p_total = p_kg * kg


if pgto == 'C':
    desc = p_total * 0.05
    p_pagar = p_total - desc
    tp_pgto = 'Cartão'
elif pgto == 'V':
    p_pagar = p_total
    tp_pgto = 'À vista'
else:
    print('Tipo de pagamento inválido. Por favor, tente novamente')

# Gera o cupom fiscal
print(f'''
Tipo de Carne: {tp_carne}
Quantidade: {kg} kg
Preço Total: R$ {p_total:.2f}
Tipo de Pagamento: {tp_pgto}
Desconto: R$ {desc:.2f}
Valor a Pagar: R$ {p_pagar:.2f}
''')
