'''
Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
conjunto de palavras
'''

i=0
lista = []

while True:
    palavra = str(input(f'Digite a {i+1}º palavra (Aperte enter para parar): '))
    i+=1
    if palavra != '':
        if 'a' in palavra:
            lista.append('a')

    else:
        break

print(f'Há {lista.count('a')} letras "a" nas palavras inseridas')