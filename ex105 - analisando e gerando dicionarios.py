def notas(*notas, sit=False):
    """ -> Função para analisar notas e situações de varios alunos.
    """
    resp = {}
    total = len(notas)
    resp['total'] = total
    resp['maior'] = max(notas)
    resp['menor'] = min(notas)
    media = sum(notas)/total
    resp['média'] = media
    if sit:
        if media < 4:
            resp['situação'] = 'PESSIMO'
        elif media >= 4 and media < 6:
            resp['situação'] = 'RUIM'
        elif media >= 6 and media < 8:
            resp['situação'] = 'RAZOAVEL'
        elif media >= 8:
            resp['situação'] = 'OTIMA'
    return resp

#Programa principal
resp = notas(10, 10, 10, sit = True)
print(resp)
