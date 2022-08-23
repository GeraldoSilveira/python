cont = 0

nomes=[]
medias=[]

while (True):
    nome = input('Digite seu nome: ')
    media = float(input('Digite sua media: '))
    print(len(nomes))
    
    cont += 1
    
    if media >= 7:
        nomes.append(nome)
        medias.append(media)
    else:
        pass
    
    if cont == 3:
        break
for item in nomes:
    print(item)