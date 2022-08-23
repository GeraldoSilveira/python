nome = input('Digite o nome do funcionario: ')
salario = float(input('digite o valor de salario para calcular: '))

if salario <= 280:
    salarioatualizado = salario * ((20/100)+1)
elif salario > 280 and salario <= 700:
    salarioatualizado = salario * ((15/100)+1)
elif salario > 700 and salario < 1500:
    salarioatualizado = salario * ((10/100)+1)
else:
    salarioatualizado = salario * ((15/100)+1)
    
print(f'O Salario de {nome} atualizado é : {round(salarioatualizado,2)}')