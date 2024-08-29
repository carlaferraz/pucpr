'''
Criar um programa que solicita ao usuário 10 números, contando
quantos são pares e quantos são ímpares. Informar ao final estas
informações
'''


#usando for
'''
pares = 0
impares = 0

for i in range(0, 10):
    num = int(input(f'Digite o {i + 1}º + número: '))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Números pares: {pares} Números ímpares: {impares}')
'''

# usando while

i=0
pares=0
impares=0


while i >=0 and i <10:
    n = int(input(f'Digite o {i+1}º número: '))
    i+=1

    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Números pares: {pares} Números ímpares: {impares}')




