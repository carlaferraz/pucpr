'''
CÁLCULO DE IMPOSTO DE RENDA MENSAL DA PESSOA FÍSICA (IRPF)
1. Coletar os seguintes dados do usuário:
- renda mensal;
- número de dependentes;
- valor da pensão alimentícia;
- outras deduções.
2. Calcular a base de cálculo:
base de cálculo = renda mensal – [(dedução por dependente * número de dependentes) + valor da pensão alimentícia + outras deduções]
- O valor da dedução é de R$ 189,59 mensais, por dependente.
3. Calcular imposto a pagar de acordo com as faixas de renda:
imposto = base de cálculo * Aliquota
- Faixa 1: Alíquota de 0% com renda mensal até 1.903,98
- Faixa 2: Alíquota de 7,5% com renda mensal até 2.826,65
- Faixa 3: Alíquota de 15,0% com renda mensal até 3.751,05
- Faixa 4: Alíquota de 22,5% com renda mensal até 4.664,68
- Faixa 5: Alíquota de 27,5% com renda mensal acima de 4.664,68
4. Registrar a faixa e alíquota utilizada mostrar nos resultados.
5. Calcular a alíquota efetiva do IRPF:
alíquota efetiva = imposto / base de cálculo
6. Imprimir os resultados com duas casas decimais:
- valor do imposto a pagar;
- faixa e alíquota em que a renda se enquadra;
- alíquota efetiva.
'''

renda = float(input('Qual sua renda mensal?: '))
dependentes = int(input('Qual o número de dependentes?: '))
pensao = float(input('Qual o valor da pensão alimentícia?: '))
outros = float(input('Digite o valor de qualquer outra dedução: '))

deduçao_dependentes = 189.59 * dependentes

base_calculo = renda - deduçao_dependentes + pensao + outros 


if base_calculo <= 1903.98:
    aliquota = 0
    faixa = 'Faixa 1'
elif base_calculo <= 2826.65:
    aliquota = 0.075
    faixa = 'Faixa 2'
elif base_calculo <= 3751.05:
    aliquota = 0.15
    faixa = 'Faixa 3'
elif base_calculo <= 4664.68:
    aliquota = 0.225
    faixa = 'Faixa 4'
else:
    aliquota = 0.275
    faixa = 'Faixa 5'

imposto = base_calculo * aliquota

aliquota_efetiva = imposto / base_calculo

print (f'''
       Conforme sua base de cálculo de R${base_calculo:.2f}, você:
       Pagará R${imposto:.2f} de imposto;
       Sua alíquota é de {aliquota:.2f}%, portanto se enquadra na {faixa};
       Sua alíquota efetiva é de {aliquota_efetiva*100:.2f}%
       ''')