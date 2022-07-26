lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    if input('Deseja continuar? [S/N]') in 'nN':
        break
print('-='*30)
print(f'A lista completa é {lista}\n'
      f'A lista de pares é {pares}\n'
      f'A Lista de impares é {impares}')
