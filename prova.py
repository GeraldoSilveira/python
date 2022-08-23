nome = input('Digite seu nome completo: ')
valorhora = float(input('Por favor informe o valor da sua hora em R$: '))
horastrabalhadas = int(input('Por favor digite a quantidades de horas trabalhadas no mês: '))
inss = 10
fgts = 11
sindicato = 3
salariobruto = valorhora * horastrabalhadas
inss_calc = salariobruto * ((10/100))
sindicato_calc = salariobruto * ((3/100))
fgts_calc = salariobruto * ((11/100))


if salariobruto <= 900:
    ir = 0
        
elif salariobruto > 900 and salariobruto <= 1500:
    ir = 5
    
elif salariobruto > 1500 and salariobruto <= 2500:
    ir = 10
else:
    ir = 20
    
ir_calc = salariobruto * ((ir/100))    

print(f'O seu Sálario Bruto é ({horastrabalhadas} * {valorhora})',9*' ',f'R$ {salariobruto:.2f}')
print(f'(-) O desconto do seu IR é: {ir}%',13*' ',f'R$ {ir_calc:.2f}')
print(f'(-) O desconto do seu INSS é: {inss}%',10*' ',f'R$ {inss_calc:.2f}')
print(f'(-) O desconto do seu Síndicato é: {sindicato}%',6*' ',f'R$ {sindicato_calc:.2f}')
print(f'O seu FGTS é  {fgts}%',26*' ',f'R$ {fgts_calc:.2f}')



totaldedescontos = ir_calc + inss_calc + sindicato_calc

print(f'\nO total de descontos em folha são de R$ {totaldedescontos}\n')

print(f'\nO Salario liquido de {nome} é R$ {salariobruto - totaldedescontos:.2f}')