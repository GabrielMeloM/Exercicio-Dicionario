'''
Crie uma função conta_letras que recebe uma palavra e retorna
um dicionário com o número de ocorrências de cada letra.
'''


def conta_letras(palavra):
    lista_letra = []
    conta = {}
    for palavra in palavra:
        lista_letra.append(palavra)
    for letra in lista_letra:
        if letra not in conta:
            conta[letra] = 1
        else:
            conta[letra] = conta[letra] + 1
    return conta


print(conta_letras("GitHub"))
