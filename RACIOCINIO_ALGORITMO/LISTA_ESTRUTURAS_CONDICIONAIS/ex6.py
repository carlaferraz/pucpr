'''
Faça um Programa que leia três números e mostre o maior deles
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))


#resposta extensa
'''
if n1>=n2 and n1>=n3:
    print(f'o número {n1} é o maior')
elif n2>=n3 and n2>=n1:
    print(f'o número {n2} é o maior')
else:
    print(f'o número {n3} é o maior')
'''

#resposta compacta
#usando a função max() para descobrir o maior número
maior = max(n1, n2, n3)
print(f'O número {maior} é o maior')