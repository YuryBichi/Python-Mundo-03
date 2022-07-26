from random import randint
from time import sleep

dados = {}
print('== SORTEANDO VALORES ==')
for j in range(1, 5):
    dados[f'jogador{j}'] = randint(1, 6)

for k, v in dados.items():
    print(f'    - o {k} tirou {v} !')
    sleep(1)
print('_-'*30)
print('== RANKING DOS JOGADORES ==')
n = 1

for i in sorted(dados, key=dados.get, reverse=True):
    print(f'    {n}º lugar: {i} com {dados[i]} !')
    n += 1
    sleep(1)
