lista = []
for cont in range(0, 5):
    lista.append(int(input('Digite um valor para lista: ')))
for c, v in enumerate(lista):

print(f'Achei o menor valor {min(lista)} na posição {c}!\n'
      f'Achei o maior alor {max(lista)} na posição {c}')
