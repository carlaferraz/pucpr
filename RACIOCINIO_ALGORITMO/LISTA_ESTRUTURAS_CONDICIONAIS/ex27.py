'''
Uma banca do Mercado Municipal está vendendo frutas com a seguinte tabela de preços:

FRUTA       ATÉ 5KG             ACIMA DE 5KG
MORANGO     R$ 15,50 KG         R$ 14,20 KG
MAÇÃ        R$ 12,80 KG         R$ 11,50 KG

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 50,00, receberá um desconto de
10% sobre o total a pagar. Escreva um programa para ler a quantidade (em Kg) de morangos e de maças adquiridas e
escreva o valor total da compra, o desconto aplicado e o valor a ser pago pelo cliente.

'''


morango_ate_5kg = 15.50
morango_mais_5kg = 14.20
maca_ate_5kg = 12.80
maca_mais_5kg = 11.50


kg_morango = float(input('Digite a quantidade de morangos (em kg): '))
kg_maca = float(input('Digite a quantidade de maçãs (em kg): '))


if kg_morango <= 5:
    valor_morango = kg_morango * morango_ate_5kg
else:
    valor_morango = kg_morango * morango_mais_5kg


if kg_maca <= 5:
    valor_maca = kg_maca * maca_ate_5kg
else:
    valor_maca = kg_maca * maca_mais_5kg


valor = valor_morango + valor_maca


if (kg_morango + kg_maca > 8) or (valor > 50):
    desconto = valor * 0.10
else:
    desconto = 0


valortotal = valor - desconto

print(f'''
Valor total da compra: R$ {valortotal:.2f}
Desconto aplicado: R$ {desconto:.2f}
Valor a ser pago: R$ {valortotal:.2f}
''')

