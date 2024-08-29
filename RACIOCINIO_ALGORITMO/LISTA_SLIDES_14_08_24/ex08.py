'''
Criar um programa que gera a série de Fibonacci até enquanto o
valor for menor que um valor informado pelo usuário. Obs.: Série de
Fibonacci = 0, 1, 1, 2, 3, 5, 8 ,13, 21, 34, 55,... é formada por 0, 1 e
partir deste ponto sempre será a soma dos dois valores anteriores
'''

#situacao de repeticao infinita: uso de while

n = int(input('Digite um número: '))

a=0
b=1


while a < n:
    print(a)
    c = b
    d = a + b

    a = c
    b = d

    

    
    

    