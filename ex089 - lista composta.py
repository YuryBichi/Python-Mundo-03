turma = []
while True:
    print()
    nome = str(input('Nome: ').title)
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    turma.append([nome, [nota1, nota2], media])

    # Interrompe o loop
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break

print()
print('-='*30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":<8}')

for i, a in enumerate(turma):
    print('-'*25)
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')

print()
print('-='*30)
while True:
    perg = int(input('Deseja ver a nota de qual aluno?(999 interrompe)'))
    print()
    if perg == 999:
        print('FINALIZANDO...')
        break
    if perg <= len(turma) - 1:
        print(f'As notas de {turma[perg][0]} são {turma[perg][1]} !')
print('<<<  VOLTE SEMPRE  >>>')
