'''
Elaborar um programa que receba um número em binário, e mostre o seu valor em
decimal
'''

numero = (input('Digite um número binário: '))
lista_numero = []
lista_decimal = []


for i in numero:
    lista_numero.append(int(i))




for i in range(len(lista_numero)):

    expoente = len(lista_numero) - 1 - i
    binario = lista_numero[i]

    lista_decimal.append((2**expoente)*binario)
    decimal = sum(lista_decimal)
        


print(f'O valor do número {numero} em decimal é igual a {decimal}')
