from time import sleep


def titulo(msg):
    tam = len(msg) + 8
    print('~' * tam)
    print(f'    {msg}')
    print('~' * tam)


def maior(lista):
    print(f'O maior número digitado foi {max(lista)} !')


#Progama principal
titulo('Função descobre maior')
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        resp = str(input('Continuar[S/N]? ').upper()[0])
        if resp == 'S' or resp == 'N':
            break
    if resp == 'N':
        print('Analisando dados',end='')
        for c in range(0, 10):
            print('.', end='', flush=True)
            sleep(0.5)
        print()
        break

maior(lista)
