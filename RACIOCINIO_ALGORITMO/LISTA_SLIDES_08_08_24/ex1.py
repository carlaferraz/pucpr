''' 
1) Elaborar um algoritmo que solicita dois números ao usuário e exibe a soma destes números, caso o segundo seja o maior ou os números sejam iguais, ou a subtração deles, caso o primeiro seja o maior 

'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

#forma extensa
'''
if n2 >= n1:
    print ('A soma dos números é:', n1 + n2)
else:
    print ('A subtração dos números é:', n1 - n2)
'''

#forma simplificada
#usando a formatação de resultado print(f'{}') para compactar o código
print (f'A soma de {n1} e {n2} é: {n1 + n2}' if n2 >= n1 else f'A subtração dos números {n1} e {n2} é: {n1 - n2}')
