#Escreva um programa que solicite ao usuario o nome do aluno e três notas.
#Guarde em um dicionario com a chave s3ndo o nome do aluno e as notas com valores 
# para cada chave.
#Ao final imprima a media de alunos.


escola={}
resp ='S'
cont = 0
soma = 0
media = 0



while(True):
    lista = []
    aluno = str (input(' Forneça seu nome '))
    nota  = float(input(' Digite a sua nota: '))
    nota1  = float(input(' Digite a sua nota: '))
    nota2  = float(input(' Digite a sua nota: '))

    lista.append(nota)
    lista.append(nota1)
    lista.append(nota2)

    escola [aluno] = lista



    resp = input('Deseja cadastrar outra nota? (S/N)')
    cont += 1

    if resp in 'Nn':
         break

for i in lista:
    soma += i

    soma = sum(lista)
    
soma = sum(lista)



for item in escola.items():

    media = soma / cont

    print( item[0]," - ", item[1])
    print(f' A média é {media}')
