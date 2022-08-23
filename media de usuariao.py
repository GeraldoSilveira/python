somaidade = 0
cont1 = 0
idade1858 = 0
somaidade2 = 0
cont2 = 0
somaidade3 =0
cont3 = 0

for c in range (1,6):
    idade = int(input('digite a idade do aluno:'))
    if idade < 18:
        somaidade += idade
        cont1 += 1

     
    if idade >= 18 and idade <= 58:
        somaidade2 += idade
        cont2 += 1
    
    if idade >= 58:
        somaidade3 += idade
        cont3 += 1

media18 = (somaidade)/cont1
print(media18)
media1858 = (somaidade2)/cont2
print(media1858)
media59 = (somaidade3)/cont3
print(media59)


