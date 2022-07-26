classif = 'Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',\
          'Fluminense', 'América-MG', 'Atletico-GO', 'Santos', 'Ceará', 'Internacional',\
          'São Paulo', 'Atletico-PR', 'Cuiabá', 'Juventude', 'Gremio', 'Bahia', 'Sport', 'Chapecoense'

print(f'Os 5 Primeiros colocados são {classif[:5]} !')
print(f'Os 4 ultimos são {classif[-4:]} !')
print(f'Ordem Alfabetica {sorted(classif)} !')
print('A Chapecoense está em {}ª na classificação !'.format(classif.index('Chapecoense') + 1))
