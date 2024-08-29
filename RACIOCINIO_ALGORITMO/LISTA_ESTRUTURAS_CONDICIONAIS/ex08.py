'''
Faça um programa que pergunte o nome e o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
'''

nome1 = str(input('Digite o nome de um produto: '))
valor1= float(input(f'Digite o valor do produto {nome1}: R$ '))
nome2 = str(input('Digite o nome de um produto: '))
valor2= float(input(f'Digite o valor do produto {nome2}: R$ '))
nome3 = str(input('Digite o nome de um produto: '))
valor3= float(input(f'Digite o valor do produto {nome3}: R$'))


if valor1 < valor2 and valor1 < valor3:
    produto = nome1
    menor = valor1
elif valor2 <valor1 and valor2 < valor3:
    produto = nome2
    menor = valor2
else:
    produto = nome3
    menor = valor3

print(f'De acordo com os dados inseridos, sugiro comprar o produto "{produto}" de valor R${menor:.2f}')