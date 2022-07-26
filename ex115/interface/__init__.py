from time import sleep

def linha(tam = 40):
    print('─' * tam)


def titulo(msg):
    linha()
    print(f'{msg:^40}'.upper())
    linha()


def leia_int(msg):
    while True:
        n1 = str(input(msg))
        try:
            valor = int(n1)
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um valor do tipo inteiro valido.\033[m')
            continue
        else:
            return valor

def abre_menu(lista):
    while True:
        titulo('menu principal')
        c = 1
        for item in lista:
            print(f'\033[;31m{c}\033[m - \033[;34m{item}\033[m')
            c += 1
        linha()
        opçao = leia_int('Sua opção: ')
        return opçao
            
        


