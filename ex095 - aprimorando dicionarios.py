import sunau

print('>> CADASTRO JOGADOR <<')
lista = []
gols = []
jogador = {}
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome: ').capitalize())
    partidas = int(input(f'Partidas que {jogador["nome"]} jogou: '))
    if partidas != 0:
        for p in range(0, partidas):
            gols.append(int(input(f'    Quantos gols na partida {p}: ')))
        jogador['gols'] = gols[:]
        jogador['total'] = sum(gols)
        lista.append(jogador.copy())

        while True:
            resp = str(input('Quer continuar? [S/N]').upper()[0])
            if resp in 'SN':
                break
            print('Erro. Digite apenas S ou N.')
        if resp == 'N':
            break
        
print('-='*25)
print(f'{"cod":<5}{"nome":<17}{"gols":<20}{"total":<15}')
print('--'*25)
for n, j in enumerate(lista):
    print(f'{n:^5}{j["nome"]:<17}{str(j["gols"]):<20}{str(j["total"]):<15}')
    if n == len(lista) -1:
        print('--'*25)
while True:
    resp1 = int(input('Mostrar dados de qual jogador? (999 para encerrar)'))
    if resp1 == 999:
        break
    print(f'- Levantando dados de {lista[resp1]["nome"]}')
    for n, gp in enumerate(lista[resp1]["gols"]):
        print(f"    Na partida {n} fez {gp} gols.")
    print('--'*25)
print('>>VOLTE SEMPRE<<')