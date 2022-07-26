import sunau

print('>> CADASTRO JOGADOR <<')

gols = []
jogador = {}
jogador['nome'] = str(input('Nome: '))
partidas = int(input(f'Partidas que {jogador["nome"]} jogou: '))
if partidas != 0:
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {p}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

print('-='*25)
print(jogador)
print('-='*25)
for k, v in jogador.items():
    print(f' O campo {k} tem o valor {v} !')
if partidas != 0:
    print('-='*25)
    print(f' O jogador {jogador["nome"]} jogou {partidas} partidas.')
    for p, g in enumerate(gols):
        print(f'    - Na partida {p} marcou {g} !')
    print(f'Foi um total de {jogador["total"] } gols!')
