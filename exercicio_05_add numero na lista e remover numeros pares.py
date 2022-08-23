

# POP() tira o item pela ordem que ele representa
'''

listas =[1,2,5,7,9,0]
listas.pop(2)
print(listas)


# adicionar todos os numeros na lista e remover somente os numeros pares

pares =[]
numeros = []
for cont in range(0,10):
    print(cont)

    numero = int(input('Digite um numero inteiro: '))
    numeros.append(numero)
    
cont1 = len(numeros)

for a in range(0,cont1):
    if numeros[a] % 2 == 0:
        pares.append(numeros[a])
        

for p in pares:
    numeros.remove(p)
       
          
print(f'Os numeros impares da lista são: {numeros}')

'''

listas=[]
listaimpares= []
for i in range(0,10):
    numero=int(input("Digite um numero"))
    listas.append(numero)
for i in range(0,len(listas)):
    if listas[i] %2!=0:
        listaimpares.append(listas[i])
        print(listaimpares)
