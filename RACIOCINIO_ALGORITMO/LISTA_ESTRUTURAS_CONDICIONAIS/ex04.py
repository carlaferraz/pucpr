'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante
'''

letra = str(input('Digite uma letra: '))

if letra == 'a':
    mensagem = ('vogal')
elif letra =='e':
    mensagem = ('vogal')
elif letra =='i':
    mensagem = ('vogal')
elif letra =='o':
    mensagem = ('vogal')
elif letra =='u':
    mensagem = ('vogal')
else:
    mensagem = ('consoante')


print(f'a letra "{letra}" é {mensagem}')