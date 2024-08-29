'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento
'''

num = float(input('Digite um número: '))

num_int = int(num)

print(f'O número {num} é inteiro.' if num == num_int else f'O número {num} é decimal')