usuario = {}
lista = []
soma_idade = 0
while True:
    usuario.clear
    usuario['nome'] = str(input('Nome: ').capitalize())
    while True:
        usuario['sexo'] = str(input(f'Sexo: [M/F] ').upper()[0])
        if usuario['sexo'] in 'MF':
            break
        print('ERRO. Por favor, digite apenas M ou F.')
    usuario['idade'] = int(input(f'Idade: ' ))
    soma_idade += usuario['idade']
    lista.append(usuario.copy())
    while True:
        resp = str(input('Deseja continuar: [S/N] ').upper()[0])
        if resp in 'SN':
            break
        print('ERRO. Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
media_idade = soma_idade/len(lista)
print('-='*30)
print(f'A) Quantas pessoas foram cadastradas: {len(lista)}')
print(f'B) A média da idade: {media_idade}') 
print('C) Lista de mulheres: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('D) Lista de pessoas com idade acima da média: ')
for p in lista:
    if p['idade'] >= media_idade:
        print(f'- {p["nome"]} com {p["idade"]} anos.')
