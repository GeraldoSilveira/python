def letra_retirar(n1,l1):
    nome_atualizado = ''
    for letra in n1:
        if letra == l1:
            letra =''
        else:
            nome_atualizado += letra
    return nome_atualizado
            
            




nome = input('Digite um nome: ')
letra_ret = input('Digite a letra a retirar: ')
palavra_sem_letra = letra_retirar(nome.lower(),letra_ret.lower())
print(f'A palavra ficou assim: {palavra_sem_letra}')