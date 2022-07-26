lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continua = str(input('Deseja continuar: [S/N]'))
    if continua in 'Nn':
        break
lista.sort(reverse=True)
print('-='*30)
print(f'Foram digitados {len(lista)} numeros!\n'
      f'Lista ordem decrescente é {lista}')
if 5 in lista:
    print('Existe o número 5 na lista!')
else:
    print('Não existe o número 5 na lista!')
