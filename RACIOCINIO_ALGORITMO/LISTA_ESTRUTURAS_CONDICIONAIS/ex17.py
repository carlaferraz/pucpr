'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano
é ou não bissexto.
'''

'''
ANO BISSEXTO:
>divisivel por 4:
    > nao pode ser divisivel por 100
    > pode ser divisivel por 400
> divisivel por 400
'''

ano = int(input('Digite um ano: '))


#resposta extensa
if ano % 400 == 0:
    print (f'O ano {ano} é bissexto!')
elif ano % 100 == 0:
    print (f'O ano {ano} é bissexto!')
elif ano % 4 == 0:
    print(f'O ano {ano} não é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')



#resposta compacta
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')