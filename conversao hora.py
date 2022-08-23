# soma de 3 parametros

'''

def soma3(n1,n2,n3):
    return(n1+n2+n3)

resp = soma3(10,15,20)
print(resp)

'''
def conv(hr,min):
    if hr > 12  and hr <= 24:
        hr += -12
        return hr, min,'PM'
    else:
        return hr, min,'AM'

resp2 = 'S'
while resp2 in 'Ss':
    
    hora = int(input('Informe sua hora: '))
    minutos = int(input('Informe os minutos: '))
    resp = conv(hora,minutos)
    
    print(f'A hora é {resp[0]} : {resp[1]} {resp[2]}')
    resp2 = input('Deseja continuar (S/N): ')
