'''
Crie uma função consulta que recebe uma agenda (um dicionário)
e uma pessoa, e retorna o telefone dessa pessoa
'''


def consulta(agenda, pessoa):
    if pessoa in agenda:
        return agenda[pessoa]
