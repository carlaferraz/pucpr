'''
Criar um programa que solicita um número ao usuário e exibe a
tabuada deste número de 1 a 10, no formato:

TABUADA DO n1
n x 1 = n
n x 2 = 2n
...
'''


#usando for
'''
n = int(input('Digite um número: '))

for i in range (1,11):
    m = n*i

    print(n, 'x', i, '=', m)
'''


#usando while

n = int(input('Digite um número: '))

i = 0

while i <= 10:
    m = n * i
    

    print(n, 'x', i, '=', m)

    i += 1




