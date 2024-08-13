'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante
'''

letra = str(input('Digite uma letra: '))

'''
#usando a função de listas []
if letra in ['a', 'e', 'i', 'o', 'u']:
    print(f'A letra {letra} é vogal')
else:
    print(f'a letra {letra} é consoante')
'''

print(f'a letra {letra} é vogal' if letra in 'aeiou' else f'a letra {letra} é consoante')