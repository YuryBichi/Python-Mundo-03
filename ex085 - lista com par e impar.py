numeros = [[], []]
for c in range(1, 8):
    temp = int(input(f'Digite o {c}º número: '))
    if temp % 2 == 0:
        numeros[0].append(temp)
    else:
        numeros[1].append(temp)
numeros[0].sort()
numeros[1].sort()
print('-='*30)
print(f'Os numeros pares digitados são: {numeros[0]}')
print(f'Os números inpares digitados são: {numeros[1]}')
