'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo
'''

n = int(input('Digite um número: '))

#resposta extensa
'''
if n>=0:
    print(f'{n} é um número positivo')
else:
    print(f'{n} é um número negativo')
'''
#resposta compacta
print(f'{n} é um número positivo' if n>=0 else f'{n} é um número negativo')