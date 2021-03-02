'''
Crie uma função telefone_principal, que recebe uma agenda
e uma pessoa.
Ela retorna o primeiro telefone da lista de telefones da
pessoa

'''


def telefone_principal(agenda, pessoa):
    if pessoa in agenda:
        return agenda[pessoa]["telefones"][0]
