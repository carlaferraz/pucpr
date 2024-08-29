'''
Faça um Programa que leia três números e mostre o maior e o menor deles, e também informe se são iguais entre si
'''


n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

if n1 == n2 == n3:
    mensagem = ('Os números são iguais')
else:
    mensagem = (f'''
MAIOR = {maior}
MENOR = {menor}''')

print(mensagem)