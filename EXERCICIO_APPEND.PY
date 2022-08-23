''''''
lista = []
resp ='S'
cont = 0
soma = 0
media = 0



while(True):
    nota  = float(input('Digite a sua nota: '))
    lista.append(nota)
    resp = input('Deseja cadastrar outra nota? (S/N)')
    cont += 1

    if resp in 'Nn':
         break

'''for i in lista:
    soma += i

    troquei por

    soma = sum(lista)
    '''
soma = sum(lista)

media = soma / cont
print(f'A média é {media}')
'''