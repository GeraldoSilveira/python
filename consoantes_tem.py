lista = ['a','b','a','b','a','b','a','b','f','g','e']

tamanho_lista = len(lista)-1
contador = 0
for a in range (tamanho_lista,-1,-1):
    if lista[a] == 'a' or lista[a] == 'e' or lista[a] == 'i' or lista[a] == 'o' or lista[a] == 'u':
        pass
    else:
        contador += 1

print (contador)