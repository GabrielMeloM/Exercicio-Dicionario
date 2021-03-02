'''
Crie uma função verifica, que recebe uma agenda
e um nome de pessoa, e verifica se a pessoa
está na agenda (retorna True se
a pessoa está e False caso contrário)
'''


def verifica(agenda, pessoa):
    if pessoa in agenda:
        return True
    else:
        return False
