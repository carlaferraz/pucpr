'''
Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano,
e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever
um programa em Python que seja capaz de calcular e iterativamente e no fim imprimir o
tempo necessário para que a população do país A ultrapasse a população do país B.
'''

pop_a = 5000000
pop_b = 7000000
ano = 0

while pop_a < pop_b:
    natalidade_a = pop_a * 0.03
    pop_a += natalidade_a

    natalidade_b = pop_b * 0.02
    pop_b += natalidade_b

    ano += 1

print(f'''
POPULAÇÃO A: {pop_a:.0f}
POPULAÇÃO B: {pop_b:.0f}
TEMPO: {ano} anos
''')
