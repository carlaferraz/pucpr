'''
Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em
consideração os anos bissextos).
'''
data1 = str(input('Digite uma data no formato dd/mm/aaaa: '))
data2= str(input('Digite uma segunda data no formato dd/mm/aaaa: '))

partes1 = data1.split('/')
partes2 = data2.split('/')

dia1 = int(partes1[0])
mes1 = int(partes1[1])
ano1 = int(partes1[2])

dia2 = int(partes2[0])
mes2 = int(partes2[1])
ano2 = int(partes2[2])


bissexto1 = (ano1 % 4 == 0 and ano1 % 100 != 0) or (ano1 % 400 == 0)
bissexto2 = (ano2 % 4 == 0 and ano2 % 100 != 0) or (ano2 % 400 == 0)


if bissexto1:
    jan1 = list(range(1, 32))
    fev1 = list(range(32, 60)) 
    mar1 = list(range(60, 91))
    abr1 = list(range(91, 121))
    mai1 = list(range(121, 152))
    jun1 = list(range(152, 182))
    jul1 = list(range(182, 213))
    ago1 = list(range(213, 244))
    set1 = list(range(244, 275))
    out1 = list(range(275, 306))
    nov1 = list(range(306, 336))
    dez1 = list(range(336, 367))
else:
    jan1 = list(range(1, 32))
    fev1 = list(range(32, 59)) 
    mar1 = list(range(59, 90))
    abr1 = list(range(90, 120))
    mai1 = list(range(120, 151))
    jun1 = list(range(151, 181))
    jul1 = list(range(181, 212))
    ago1 = list(range(212, 243))
    set1 = list(range(243, 274))
    out1 = list(range(274, 305))
    nov1 = list(range(305, 335))
    dez1 = list(range(335, 366))

if bissexto2:
    jan2 = list(range(1, 32))
    fev2 = list(range(32, 60)) 
    mar2 = list(range(60, 91))
    abr2 = list(range(91, 121))
    mai2 = list(range(121, 152))
    jun2 = list(range(152, 182))
    jul2 = list(range(182, 213))
    ago2 = list(range(213, 244))
    set2 = list(range(244, 275))
    out2 = list(range(275, 306))
    nov2 = list(range(306, 336))
    dez2 = list(range(336, 367))
else:
    jan2 = list(range(1, 32))
    fev2 = list(range(32, 59)) 
    mar2 = list(range(59, 90))
    abr2 = list(range(90, 120))
    mai2 = list(range(120, 151))
    jun2 = list(range(151, 181))
    jul2 = list(range(181, 212))
    ago2 = list(range(212, 243))
    set2 = list(range(243, 274))
    out2 = list(range(274, 305))
    nov2 = list(range(305, 335))
    dez2 = list(range(335, 366))


meses1 = [jan1, fev1, mar1, abr1, mai1, jun1, jul1, ago1, set1, out1, nov1, dez1]
meses2 = [jan2, fev2, mar2, abr2, mai2, jun2, jul2, ago2, set2, out2, nov2, dez2]


dias_ate_mes_1 = 0
dias_ate_mes_2 = 0




for i in range(mes1 - 1):
    dias_ate_mes_1 += len(meses1[i])

for i in range(mes2 - 1):
    dias_ate_mes_2 += len(meses2[i])


dias_passados_1 = dias_ate_mes_1 + dia1
dias_passados_2 = dias_ate_mes_2 + dia2





dias_totais_ano1 = 0
for ano in range(ano1):
    dias_totais_ano1 += 366 if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else 365

dias_totais_ano2 = 0
for ano in range(ano2):
    dias_totais_ano2 += 366 if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else 365





dias_totais_1 = dias_totais_ano1 + dias_passados_1
dias_totais_2 = dias_totais_ano2 + dias_passados_2


diferenca = int(dias_totais_2) - int(dias_totais_1)

if diferenca < 0:
    diferenca = -diferenca


print(f'A diferença entre as datas {data1} e {data2} é igual a {diferenca} dias')
