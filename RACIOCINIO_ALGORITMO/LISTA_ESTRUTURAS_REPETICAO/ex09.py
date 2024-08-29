'''
Elaborar um programa em Python que converta um número decimal em hexadecimal,
fazendo uso do método de divisões sucessivas
'''

# 0 1 2 3 4 5 6 7 8 9 A B C D E F

numero_decimal = int(input('Digite um número: '))




i=0

quociente = numero_decimal // 16

resto = numero_decimal/16 - quociente

lista_quociente = []
lista_resto = []


lista_quociente.append(quociente)
lista_resto.append(resto*16)




while quociente > 0:
    quociente2 = quociente / 16
    quociente = quociente // 16
   
    resto = quociente2 - quociente
   
    

    lista_quociente.append(quociente)
    lista_resto.append(resto*16)


letras = ['A', 'B', 'C', 'D', 'E', 'F']
hexadecimal = []

for a in range(len(lista_resto)-1,-1,-1):

    if lista_resto[a] > 10:
        index = int(lista_resto[a] - 10)
        hexadecimal.append(letras[index])
    else:
        hexadecimal.append(str(int(lista_resto[a])))




resultado=''

for item in hexadecimal:
    resultado = resultado + item


print(f'O resultado em hexadecimal é igual a {resultado}')

