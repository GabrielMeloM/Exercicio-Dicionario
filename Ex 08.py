'''
Crie uma função conta telefones, que recebe uma agenda (nessa versão
mais nova) e retorna a quantidade de números de telefone registrados.

Se houver telefones repetidos, conte as repetições
'''


def conta_telefones(agenda):
    lista = []
    soma = 0
    for pessoa, valor in agenda.items():
        if 'telefones' in agenda[pessoa]:
            lista.append(agenda[pessoa]["telefones"])
    for i in range(len(lista)):
        soma += len(lista[i])
    return soma
