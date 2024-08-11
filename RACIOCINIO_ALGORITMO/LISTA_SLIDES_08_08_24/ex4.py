'''
Criar um programa que solicita ao usuário o seu salário. Se o valor informado for inferior a 5.000 calcule um abono de final de ano de 15%. Caso contrário, o abono será de 10%. Informe ao usuário seu valor de abono de final de ano
'''

salario = float(input('Digite seu salário: '))


#forma extensa
'''
if salario < 5000:
    abono = salario*0.15
else:
    abono = salario*0.1
'''

#forma compactada
abono = salario * 0.15 if salario<5000 else salario*0.1


salario_fim_ano = salario + abono

#usando a formatação f'{valor:formato} para ajeitar as casas decimais

print(f'Você recebeu um abono de final de ano de R${abono:.2f}! Seu salário será igual a R${salario_fim_ano:.2f}')