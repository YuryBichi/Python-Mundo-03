from random import randint
from time import sleep
umjogo = list()
jogos = list()
totjogos = 0
print('-'*30)
print('        JOGO DA MEGA       ')
print('-'*30)
quant = int(input('Quantos jogos quer sortear? '))
while totjogos < quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in umjogo:
            umjogo.append(num)
            cont += 1
        if cont >= 6:
            break
    totjogos += 1
    umjogo.sort()
    jogos.append(umjogo[:])
    umjogo.clear()

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*3, '  > BOA SORTE <  ', '=-'*3)
