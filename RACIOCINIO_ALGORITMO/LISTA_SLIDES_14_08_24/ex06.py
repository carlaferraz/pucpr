'''
Criar um programa que pede para o usuário inserir um login e uma
senha. Caso os valores sejam iguais, informar que os dados são
inválidos e pedir novamente as informações. Caso contrário, exibir a
mensagem "Bem-vindo ao sistema!!!"
'''

#condicao de validacao: uso de while

login = ''
senha = ''


while login == senha:
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')

        if login == senha:
            print ('Valores inválidos. Por favor, tente novamente.')
        else:
            print('Bem-vindo ao sistema!')

    
