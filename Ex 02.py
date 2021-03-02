'''
Crie uma função adiciona que recebe uma agenda
(um dicionário)
uma pessoa e um telefone, e adiciona o
telefone dessa pessoa na agenda

Adicionar um item num dicionário é simples
dicionario['chave'] = valor
'''


def adiciona(agenda, pessoa, telefone):
    agenda[pessoa] = telefone
    return agenda
