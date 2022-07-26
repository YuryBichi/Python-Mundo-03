from random import randint
from time import sleep

nuns = []
lisPar = []

def sortear():
    while True:
        tam = len(nuns)
        if tam < 5:
            alea = randint(1, 9)
            if alea not in nuns:
                nuns.append(alea)
        elif tam == 5:
            print(f'Sorteando os 5 numeros:', end=' ')
            for n in nuns:
                print(n, end=' ',flush=True)
                sleep(0.5)
            print('PRONTO')
            break

def somaPar():
    for n in nuns:
        if n % 2 == 0:
            lisPar.append(n)
    soma = sum(lisPar)
            
    print(f'A soma dos numeros pares de {nuns} é {soma} !')

sortear()
somaPar()