'''
Criar um programa que pede ao usuário 5 números, e informa
qual é o menor e qual é o maior deles
'''



#usando for
'''
n = int(input('Digite o 1º número: '))
menor = n
maior = n

for i in range(0, 5):
    n = int(input(f'Digite o {i + 1}º número: '))

    if n < menor:
        menor = n
    if n > maior:
        maior = n

print(f'
MAIOR: {maior}
MENOR: {menor}')
'''

#usando while
i=0
n = int(input('Digite o 1º número: '))
menor = n
maior = n

while i < 5:
    n = int(input(f'Digite o {i+1}º número: '))
    i+=1

   

    if n < menor:
        menor = n
    if n > maior:
        maior = n

print(f'''
MAIOR: {maior}
MENOR: {menor}''')

