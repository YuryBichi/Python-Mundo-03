import moeda


moeda.titulo('Trabalhando com modulos.')
pre = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(pre)} é {moeda.metade(pre, True)}')
print(f'O dobro de {moeda.moeda(pre)} é {moeda.dobro(pre, True)}')
print(f'O aumento de 10% de {moeda.moeda(pre)} é {moeda.aumenta(pre, 10, True)}')
print(f'O diminuir de 13% de {moeda.moeda(pre)} é {moeda.diminui(pre, 13, True)}')