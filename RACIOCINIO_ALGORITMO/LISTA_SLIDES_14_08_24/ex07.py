'''
Criar um programa que solicite ao usuário vários números e, ao
digitar 0, calcula a média destes números informados
'''

#condição infinita: uso de while

n=1
i=0
soma = 0

while True:
    n = int(input(f'Digite o {i+1}º número (digite "0" para parar):'))
    if n != 0:
        i+=1
        soma += n 
    else: 
        break;


if i > 0:
    media = soma / i
    print(media)
else:
    print ('Inválido, digite outro número além do "0"')

    



