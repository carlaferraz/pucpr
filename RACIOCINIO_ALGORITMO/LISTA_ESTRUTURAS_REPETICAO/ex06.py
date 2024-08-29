'''
Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
primeiro e último nome
'''

nome = str(input("Qual seu nome completo?: "))

lista_nome = []
nome_atual = ''

for i in nome:
    if i == ' ':
        if nome_atual != '':
            lista_nome.append(nome_atual)
            nome_atual=''
    else:
        nome_atual += i




if nome_atual != '':
    lista_nome.append(nome_atual)




if lista_nome != '':
    ultimo_nome = lista_nome[-1]
    primeiro_nome = lista_nome[0]


print(primeiro_nome)
print(ultimo_nome)