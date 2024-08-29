'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme oexemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220

SALÁRIO BRUTO: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS (10%): R$ 110,00
FGTS (11%): R$ 121,00
TOTAL DE DESCONTOS: R$ 165,00
SALÁRIO LÍQUIDO: R$ 935,00
'''

valor_hora = float(input('Qual o valor da sua hora trabalhada?: '))
qtd_hora = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario_bruto = (valor_hora*qtd_hora)

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = 0.05
elif salario_bruto <= 2500:
    desconto_ir = 0.10
else:
    desconto_ir = 0.20

ir = salario_bruto*desconto_ir
inss = salario_bruto*0.03
fgts = salario_bruto*0.11
total_descontos = ir+inss
salario_liquido = salario_bruto - total_descontos


print(
f'''
SALÁRIO BRUTO: (R$ {valor_hora:.2f} * {qtd_hora:.0f}) : R$ {salario_bruto:.2f}
(-) IR (5%) : R$ {ir:.2f}
(-) INSS (10%): R$ {inss:.2f}
FGTS (11%): R$ {fgts:.2f}
TOTAL DE DESCONTOS: R$ {total_descontos:.2f}
SALÁRIO LÍQUIDO: R$ {salario_liquido:.2f}
'''
)