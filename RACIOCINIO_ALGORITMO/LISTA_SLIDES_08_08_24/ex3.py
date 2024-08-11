'''
Criar um programa que solicita um número ao usuário, e informa se este número é par ou ímpar. Dica: para saber se um número é par ou ímpar calcule o resto da divisão deste número por 2 (operador %). Se o resultado for 0 o número é par, s e f o r 1 é ímpar.
'''

n = int(input('Digite um número inteiro: '))

#forma extensa
'''if n % 2 == 0:
    print(f'O número {n} é par!')
else:
    print(f'o número {n} é ímpar!')'''

#forma simplificada
print(f'O número {n} é par!' if n%2==0 else f'O número {n} é ímpar!')