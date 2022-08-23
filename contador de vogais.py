
def cont_vogaisf(vog):
    acumulador = 0
    for vogais in vog:
        if  vogais == 'a' or vogais == 'e' or vogais == 'i' or vogais == 'o' or vogais == 'u':
            acumulador += 1
        else:
            pass
    return acumulador
            
                        



vogais = input('Digite um Nome: ')
cont_vogais = cont_vogaisf(vogais.lower())
print(f'A quantidades de vogais são {cont_vogais}!')