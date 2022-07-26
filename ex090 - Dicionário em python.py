dicio = {}
dicio['nome'] = str(input('Nome: '))
dicio['média'] = float(input(f'Média de {dicio["nome"]}: '))
if dicio['média'] >= 7:
    dicio['resultado'] = 'Aprovado'
elif dicio['média'] < 7 >= 5:
    dicio['resultado'] = 'Recuperação'
else: 
    dicio['resultado'] = 'Reprovado'

print('-='*25)
for k, v in dicio.items():
    print(f'    - o {k} é igual a {v} !')
    