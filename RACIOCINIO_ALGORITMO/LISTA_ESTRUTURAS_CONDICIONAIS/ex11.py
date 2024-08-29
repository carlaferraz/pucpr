'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um
colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
• salários até R$ 1.280,00 (incluindo) : aumento de 20%;
• salários entre R$ 1.280,00 e R$ 2.700,00 : aumento de 15%;
• salários entre R$ 2.700,00 e R$ 5.000,00 : aumento de 10%;
• salários de R$ 5.000,00 em diante : aumento de 5%;
Após o aumento ser realizado, informe na tela:
• o salário antes do reajuste;
• o percentual de aumento aplicado;
• o valor do aumento;
• o novo salário, após o aumento
'''

salario = float(input("Digite o valor do seu salário atual: R$ "))

if salario <= 1280:
    novo_salario = salario * 1.2
    aumento = 0.20
elif salario <= 2700:
    novo_salario = salario * 1.15
    aumento = 0.15
elif salario <= 5000:
    novo_salario = salario * 1.1
    aumento = 0.10
else:
    novo_salario = salario * 1.05
    aumento = 0.05

print(f'''Com base nos dados fornecidos:
Salário antes do reajuste: R${salario:.2f};
Percentual de aumento aplicado: {aumento*100}%
Valor do aumento: R${aumento*salario:.2f}
Novo salário após o aumento: R${novo_salario:.2f}
      ''')


