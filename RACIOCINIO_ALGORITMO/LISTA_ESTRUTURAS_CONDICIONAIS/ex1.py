'''
Faça um Programa que peça dois números e imprima o maior deles
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))


'''
if n1 > n2:
    print(f'o número {n1} é o maior')
else:
    print(f'o número {n2} é o maior')
'''

print(f'o número {n1} é o maior' if n1 > n2 else 
f'o número {n2} é o maior')