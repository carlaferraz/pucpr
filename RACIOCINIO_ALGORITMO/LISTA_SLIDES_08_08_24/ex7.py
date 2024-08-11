'''
Criar um programa que pergunta o tamanho de três lados de um triângulo, e informa que tipo de triângulo que é, a saber:
a.Só será um triângulo quando a soma de dois lados sempre for maior que o terceiro lado;
b.Equilátero: triângulo que tem todos os lados iguais;
c.Isóceles: triângulo que tem dois lados iguais;
d.Escaleno: triângulo que tem todos os lado diferentes.
'''

n1 = float(input('Digite um lado do triângulo '))
n2 = float(input('Digite um segundo lado do triângulo '))
n3 = float(input('Por fim, digite um terceiro lado do triângulo '))


# resposta extnesa
'''
if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    print('O triângulo existe! Agora vamos ver em que categoria ele se encaixa:')
    if n1 == n2 == n3:
        print('O triângulo é equilátero')
    elif n1==n2 or n1==n3 or n2==n3:
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Os valores não formam um triângulo!')
'''

#resposta compactada
if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    triangulo= ( 
        'equilátero' if n1 == n2 == n3 else 'isósceles' if n1==n2 or n1==n3 or n2==n3 else 'escaleno'
        )
    print(f'O triângulo é do tipo {triangulo}')

else:
    print('O triângulo não existe!')