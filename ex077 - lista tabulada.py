print('-'*40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-'*40)

listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 120.32,
            'Canetas', 22.30,
            'Livro', 34.9)
for pos, produto in enumerate(listagem):
    if pos % 2 == 0:
        print(f'{produto:.<30}', end='')
    else:
        print(f'R${produto:>7.2f}')
print('-'*40)
