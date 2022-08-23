def parimpar(num1,num2):
    quantpares = 0
    
    if num1 % 2 == 0:
        quantpares += 1
    if num2 % 2 == 0:
        quantpares += 1
    else:
        pass
    return quantpares
    

num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))

result = parimpar(num1,num2)

print(f'O resultado é {result}')