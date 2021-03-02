'''
Crie uma função sem_email, que recebe uma agenda (nessa versão
mais nova) e retorna uma lista de todos os contatos sem email.
'''


def sem_email(agenda):
    lista = []
    for pessoa in agenda.keys():
        if "email" not in agenda[pessoa]:
            lista.append(pessoa)
    return lista
