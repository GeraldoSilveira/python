


def stringsemletra(palavra1,letradousuario1):
    
    letraParaExibir = ""

    for letracontador in palavra1:
        if letracontador == letradousuario1:
            pass
        elif letracontador != letradousuario1:
            letraParaExibir += letracontador
    return letraParaExibir




palavra = input('digite uma palavra: ')
letradousuario = input('digite uma letra: ')
result = stringsemletra(palavra.lower(),letradousuario.lower())
print(f'O resultado é {result}')