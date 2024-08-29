'''
Criar um programa que simula um carrinho de compras, onde
solicita o nome do produto (não pode ser vazio), o valor deste
produto (valor com vírgula, positivo) e a quantidade deste
produto a ser comprada (valor inteiro, positivo). Ao incluir um
produto, deve perguntar se o usuário deseja fechar o pedido ou
incluir mais produtos. Todos os dados devem ser validados. Ao
final da compra, deve ser informado o valor total do pedido
'''


total = 1
continuar = 1


while continuar == 1:
    try:
        print('---------- CARRINHO DE COMPRAS ------------')

        nome = str(input('Digite o nome do produto: '))
        if nome == '':
            print('O campo "nome do produto" não pode ser vazio.')
            break
        try:
            nome = int(nome)
            print('Digite apenas texto')
            break
        except:
            nome = str(nome)

            valor = float(input('Digite o valor do produto: '))
            if valor <= 0:
                print('O valor do produto deve ser diferente de 0')
                break

            quantidade = int(input('Digite a quantidade do produto: '))
            if valor <= 0:
                print('A quantidade do produto deve ser diferente de 0')
                break

            total = valor * quantidade

            continuar = int(input(
                'Digite "1" se deseja adicionais mais produtos ao seu carrinho. Digite qualquer outro número se deseja finalizar: '))
            if continuar != 1:
                print('Finalizando o pedido.')
                print(f'O total do pedido é igual a R${total:.2f}')
                break

    except ValueError:
        print('Valor inválido')
