matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite o valor de [{l}, {c}]: ')))
print('~-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('~-'*30)

print(f'A soma dos pares foi total de {somapar} !')
print(f'A soma da terceira coluna é de {matriz[0][2]+matriz[1][2]+matriz[2][2]} !')
print(f'O maior valor da segunda linha é {max(matriz[1])} !')
