'''
Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa final e o tempo calculado em segundos
'''

massa = float(input('Digite o valor inicial da massa, em gramas, do objeto: '))

tempo = 0

while massa > 0.5:
    massa = massa / 2
    tempo = tempo + 50

print(f'A massa final é igual a {massa} g e o tempo decorrido foi de {tempo} segundos')