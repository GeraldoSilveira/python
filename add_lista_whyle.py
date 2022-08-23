# Adicionando nome a lista

'''
nomes = []
while (True):
    nome = input('Digite um nome: ')
    nomes.append(nome)
    resp = input('deseja continuar (S/N): ')
    if resp in 'Nn':
        break
print(nomes)
  
   ''' 
   
# adicionando numero a lista e somando todos
'''
numeros = []
soma = 0


while(True):
    numero = float(input('Digite um numero: '))
    numeros.append(numero)
    soma += numero
    resp = input('deseja continuar (S/N): ')
    if resp in 'Nn':
        break
print(f'A soma dos numeros é {soma:.2f}')

'''

# Adiciona numero na lista e depois da a média

notas = []
soma = 0
cont = 0
while(True):
    nota = float(input('digite sua nota: )  '))
    notas.append(nota)
    soma += nota
    cont += 1
    resp = input('Deseja continuar (S/N): ')
    if resp in 'Nn':
        break
media = soma / cont

print(f'A media das notas são: {media:.2f}')

print(f'As suas notas respectivamente são: {notas}')
    
    