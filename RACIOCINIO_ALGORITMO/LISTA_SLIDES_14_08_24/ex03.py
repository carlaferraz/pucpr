'''
Criar um programa que recebe um texto digitado pelo usuário e
o imprime apenas com consoantes, removendo as vogais. Obs.:
desconsiderar letras maiúsculas e acentos.
'''



#usando for
'''
texto = str(input('Digite um texto: '))

resultado = ''

for letra in texto:
    if letra in 'bcdfghjklmnpqrstvwxyz':
        resultado += letra
'''


#usando while
texto = str(input('Digite um texto: '))
resultado=''
posicao = 0 

while posicao < len(texto):
    letra = texto[posicao]
    if letra in 'bcdfghjklmnpqrstvwxyz':
        resultado += letra
    
    posicao += 1


print(resultado)
    

