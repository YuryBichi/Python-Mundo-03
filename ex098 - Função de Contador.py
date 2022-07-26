from time import sleep


def titulo(msg):
    tam = len(msg) + 8
    print('~'*tam)
    print(f'    {msg}')
    print('~'*tam)

def contador(inc, fim, passo):
    if passo > 0:
        print(f'Contagem de {inc} a {fim} contando de {passo} em {passo}.')
        for n in range(inc, fim +1, passo):
            print(f'{n}', end=' ', flush=True)
            sleep(0.5)
        print('FIM')
    elif passo < 0:
        print(f'Contagem de {inc} a {fim} contando de {passo} em {passo}.')
        for n in range(inc, fim -1, passo):
            print(f'{n}', end=' ', flush=True)
            sleep(0.5)
        print('FIM')

# Programa principal
titulo('CONTADOR!')
contador(1, 10, 1)
contador(10, 1, -2)
titulo('CONTADOR PERSONALIZADO!')
print('Agora é sua vez de personalizar o contador!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)