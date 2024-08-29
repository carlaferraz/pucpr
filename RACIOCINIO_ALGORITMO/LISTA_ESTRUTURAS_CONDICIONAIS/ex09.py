'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))


if n1 >=n2:
    if n2>=n3:
        mensagem = (n1, n2, n3)
    elif n1>=n3:
        mensagem = (n1, n3, n2)
    else:
        mensagem = (n3, n1, n2)
else:
    if n1>=n3:
        mensagem = (n2, n1, n3)
    elif n2>=n3:
        mensagem = (n2, n3, n1)
    else:
        mensagem = (n3, n2, n1)

print('a ordem decrescente dos números é ', mensagem)

