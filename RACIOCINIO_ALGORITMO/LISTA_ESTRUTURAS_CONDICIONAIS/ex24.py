'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O
resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal.
'''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
op = str(input('Agora vamos escolher a operação a se fazer entre esses números. Digite M se deseja multiplicar, D para dividir, A para adicionar e S para substrair '))


if op =='M':
    n3 = n1 * n2
    mensagem_op = (f'{n1} * {n2} = {n3}')   
elif op =='D':
    n3 = n1 / n2
    mensagem_op = (f'{n1} / {n2} = {n3} ')
elif op =='A':
    n3 = n1 + n2 
    mensagem_op = (f'{n1} + {n2} = {n3}')
else:
    n3 = n1 - n2 
    mensagem_op = (f'{n1} - {n2} = {n3}')



mensagem_a = ('par') if n3%2==0 else 'ímpar'

mensagem_b = ('positivo') if n3 >=0 else 'negativo'

mensagem_c = ('inteiro') if n3 == int(n3) else 'decimal'

print(f'''
OPERAÇÃO: {mensagem_op}
A) O número {n3} é {mensagem_a}
B) O número {n3} é {mensagem_b}
C) O número {n3} é {mensagem_c}
''')

    


