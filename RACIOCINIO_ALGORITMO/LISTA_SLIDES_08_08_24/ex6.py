'''
Criar um programa que solicite ao usuário dois números e a operação que se deseja executar entre eles. Mostrar o resultado desta operação no formato: num1 operação num2 = resultado.
'''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
op = str(input('Agora vamos escolher a operação a se fazer entre esses números. Digite M se deseja multiplicar, D para dividir, A para adicionar e S para substrair '))


#resposta extensa
'''
if op == 'M':
    print(f'{n1} * {n2} = {n1*n2}')
elif op == 'D':
    print(f'{n1} / {n2} = {n1/n2}')
elif op == 'A':
    print(f'{n1} + {n2} = {n1+n2}')
elif op == 'S':
    print(f'{n1} - {n2} = {n1-n2}')
else:
    print('Valor inválido! Por favor, selecione entre M, D, A ou S')
'''


#resposta compacta
mensagem = (
    f'{n1} * {n2} = {n1*n2}' if op =='M' else 
    f'{n1} / {n2} = {n1/n2}' if op =='D' else
    f'{n1} + {n2} = {n1+n2}' if op =='A' else
    f'{n1} - {n2} = {n1-n2}' if op =='S' else
    'Valor inválido! Por favor, selecione entre M, D, A ou S'
)

print(mensagem)