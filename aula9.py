
#Escreva um script Python para gerar e imprimir um dicionário que 
# contenha um número (entre 1 e n) na forma (x, x*x).
'''
n=int(input("Forneça um número "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 
'''
#Escreva um script Python para imprimir um dicionário onde as chaves 
# são números entre 1 e 15 (ambos incluídos) e os valores são quadrados das chaves. 
# Acesse o Dicionário de amostra do editor {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 6
# 4, 9: 81, 10: 100, 11: 121 , 12: 144, 13: 169, 14: 196, 15: 225}

'''
quadrados = {}
for i in range(1,16):
 quadrados[i]=i**2
print(quadrados) 



dict = {}
string = input('Forneça uma palavra')
for letra in string:
    c = string.count(letra)
    dict[letra] = c
print(dict)

'''





dictletras = {}

palavra = input( " Digite uma palavra")

for letra in palavra:
    if letra in dictletras.keys():
        dictletras[letra] = dictletras[letra]+1
    else:
        dictletras[letra]=1
    print(dictletras)
    
