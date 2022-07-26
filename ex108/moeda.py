def titulo(msg):
    tam = len(msg)+4
    print('~'*tam)
    print(f'  {msg}'.upper())
    print('~'*tam)


def metade(n, m=False):
    r = n/2
    if m == True:
        r = moeda(r)
    return r


def dobro(n, m=False):
    r = n*2
    if m == True:
        r = moeda(r)
    return r


def aumenta(n, taxa, m=False):
    r = n*(1+(taxa/100))
    if m == True:
        r = moeda(r)
    return r


def diminui(n, taxa, m=False):
    r = n *(1-(taxa/100))
    if m == True:
        r = moeda(r)
    return r


def moeda(n):
    r = f'R$ {n:.2f}'
    return r


def resumo(preço, taxaa=10, taxad=5):
    print('─'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('─'*40)

    print(f'Valor analisado: \t{moeda(preço)}')
    print(f'Dobro do valor: \t{dobro(preço, True)}')
    print(f'Metade do valor: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumenta(preço, taxaa, True)}')
    print(f'{taxad}% de redução:  \t{diminui(preço, taxad, True)}')
    print('─'*40)
    