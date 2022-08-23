nomes =[]
idades =[]

for a in range(0,3):
    nome = input('Digite nome: ')
    idade = input('Digite idade ')

    idades.insert(a,idade)
    
    nomes.insert(a,nome)

for b in range(0,len(nomes)):
    print(f'{nomes[b]} tem a {idades[b]} anos de idade')
    b += 1