'''
Criar um programa que pede dois números ao usuário. O
primeiro será o numerador, e o segundo será o expoente. A saída
do programa deve ser o resultado da operação numerador
elevado a expoente. Obs.: não usar função interna que calcula
automaticamente potência
'''

#usando for
'''
n = int(input('Digite um número para atuar como numerador: '))

e = int(input('Digite um número para atuar como expoente: '))

r=1

for i in range(e):
    r *= n

print(f'{n} ^ {e} = {r}')
'''

#usando while
n = int(input('Digite um número para atuar como numerador: '))

e = int(input('Digite um número para atuar como expoente: '))

i = 0
r = 1

while i < e:
    r *= n
    i+=1

print(f'{n} ^ {e} = {r}')
