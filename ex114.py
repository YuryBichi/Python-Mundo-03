from time import sleep
import urllib.request


try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[0;31mO site pudim nao está acessível.\033[m')
else:
    print('\033[0;33mO site pudim está acessível.\033[m')
finally:
    print('Encerrando em')
    for c in range(-3, 0):
        print(f'{-c}', end='',flush=True)
        for p in range(0,3):
            print('.',end='',flush=True)
            sleep(0.5)
        print()

        