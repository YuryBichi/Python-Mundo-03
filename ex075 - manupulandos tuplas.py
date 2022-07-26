tupla = int(input('Digite um número: ')),\
        int(input('Digite outro número: ')),\
        int(input('Digite mais um número: ')),\
        int(input('Digite o ultimo número: '))
print(f'Você digitou os valores {tupla} !')

if 9 in tupla:
    print(f'O numero 9 aparece {tupla.count(9)} ', 'vez !' if tupla.count(9) == 1 else 'vezes !')
else:
    print('Não foi digitado número 9 !')

if 3 in tupla:
    print(f'O numero 3 aparece na {tupla.index(3) + 1}ª posição !')
else:
    print('Não foi digitado o numero 3 em nenhuma posição !')

print('Os valores digitados pares foram ', end='')
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=' ')
