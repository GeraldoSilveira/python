#Faça um programa para gerenciar um mercado. 
# O sistema deve possibilitar inserir itens e deletar itens. 
# Os itens serão armazenados em um dicionario onde teremos a chave como o nome e o valor como preço.
#Menu
#Digite 1 para cadastrar um item
#Digite 2 para deletar um item   pop(chave)
#Digite 3 para sair. Ao sair imprima o dicionário

produtos={}

while (True):

    menu = input(' Informe o produto a ser cadastrado e digite (1) para cadastro, digite (2) para deletar um item, e digite (3) para sair ')

    if menu == '1':

        itemcadastro = input(' Digite o item para cadastro')
        preco = input(' Digite o preço dos produtos')

        produtos[itemcadastro] = preco

    elif menu == '2':
        print(produtos)

        excluiritem = input('Qual item vai deletar')
        produtos.pop(excluiritem)

    elif menu == 3:
        for item in produtos.items():
            print(f'{item[0]} é R$ {item[1]}')
        break
    else:
        print(' Digite a opção correta.')



        '''
        
        
dictProdutos = {}

while(True):
    opcao = int(input("""
    Digite a opcao do menu
    1 - Cadastro de Item
    2 - Deleção de Item
    3 - Sair do programa 
    """))

    if opcao == 1:
        nomeProduto = input("Digite o nome do produto")
        valorProduto = float(input("Digite o valor do produto"))
        dictProdutos[nomeProduto] = valorProduto
        print("Produto cadastrado com sucesso\n")
        print(f"Sua nova lista é {dictProdutos}")
    elif opcao == 2:
        produtoDeletado = input("Digite o nome do produto a ser deletado")
        if produtoDeletado in dictProdutos.keys():
            dictProdutos.pop(produtoDeletado)
            print("Produto deletado com sucesso\n")
            print(f"Sua nova lista é {dictProdutos}")
        else:
            print("Produto não encontrado\n")
    elif opcao == 3:
        break
    
print(dictProdutos)

        
        
        
        '''
        