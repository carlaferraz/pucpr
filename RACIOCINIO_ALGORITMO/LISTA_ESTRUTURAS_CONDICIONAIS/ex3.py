'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M -
Masculino, Sexo Inválido
'''

letra = str(input('Digite F ou M: '))

'''
if letra=='F':
    print('Feminino')
if letra=='M':
    print('Masculino')
else:
    print('Inválido!')
'''

print('Feminino' if letra=='F' else 'Masculino' if letra=='M' else 'Inválido')
