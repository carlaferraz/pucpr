'''
Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
crescente
'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
n5 = int(input('Digite o quinto número: '))


for i in range (0,4):
    if n1>n2:
        a = n1
        n1 = n2
        n2 = a
    if n2>n3:
        a = n2
        n2 = n3
        n3 = a
    if n3>n4:
        a = n3
        n3 = n4
        n4 = a
    if n4>n5:
        a = n4
        n4 = n5
        n5 = a

print(n1, n2, n3, n4, n5)
