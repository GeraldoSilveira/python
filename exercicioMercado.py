#Faça um programa para gerenciar um mercado. 
# O sistema deve possibilitar inserir itens e deletar itens. 
# Os itens serão armazenados em um dicionario onde teremos a chave como o nome e o valor como preço.
#Menu
#Digite 1 para cadastrar um item
#Digite 2 para deletar um item   pop(chave)
#Digite 3 para sair. Ao sair imprima o dicionário

produtos={}

while(True):

    menu = input('''  Informe o produto a ser cadastrado,
                 1 cadastro, 2 deletar item, 
                 3 para sair ''')
     
    if menu == '1':
        
        produtocadastro = input (' Digite o item para cadastro ')
        preco = input (' Digite o preço dos produtos ')
        
        produtos[produtocadastro] = preco
        
    elif menu == '2' :
        print(produtos)
        
        excluiritem = input ( ' Qual  item vai deletar ')
        produtos.pop(excluiritem)
        
    elif menu == '3':
        
        for item in produtos.items():
        
            print(f'{item[0]} é R$ {item[1]}')
            

            
        break
        