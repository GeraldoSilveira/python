# Funções
def media(num1,num2):
    media2 = (num1 + num2)/2
    print(f'A média dos numeros informados vale {media2}')

def soma(num1,num2):
    return num1 + num2

def negpos (num1):
    if num1 > 0:
        print('Positivo')
    elif num1 < 0:
        print('Negativo')
    else:
        print('Neutro')
    


numm1 = int(input(f'digite primeiro numero: '))
numm2 = int(input(f'digite segundo numero: '))

media(numm1,numm2)
soma = soma(numm1,numm2)

negpos(numm1)


