print('-'*40)
print(f'{"LISTA DE VALORES":^40}')
print('-'*40)

lista = list()
repetidos = list()
while True:
    temp = int(input('Qual valor deseja salvar na lista: '))
    if temp in lista:
        print('Valor repetido, não será salvo...')
        repetidos.append(temp)
    else:
        lista.append(temp)
        print('Valor adicionado com sucesso...')
    continua = str(input('Deseja continuar? [S/N]  '))
    if continua in 'Nn':
        break
lista.sort()
repetidos.sort()
print('='*50, f'\nOs valores salvos na lista foram:\n'
      f'{lista}')
print(f'Os valores repetidos não salvos são:\n'
      f'{repetidos}')
