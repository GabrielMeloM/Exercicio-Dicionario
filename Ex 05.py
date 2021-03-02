'''
Crie uma função email, que recebe uma agenda
e uma pessoa.
Ela retorna o email da pessoa.
Não precisa se preocupar com
o caso do registro da pessoa nao ter email.
'''


def email(agenda, pessoa):
    if pessoa in agenda:
        return agenda[pessoa]["email"]
    else:
        return 'Email não cadastrado.'
