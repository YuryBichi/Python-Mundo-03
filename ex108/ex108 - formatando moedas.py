import moeda


moeda.titulo('Trabalhando com modulos.')
pre = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(pre)} é {moeda.moeda(moeda.metade(pre))}')
print(f'O dobro de {moeda.moeda(pre)} é {moeda.moeda(moeda.dobro(pre))}')
print(f'O aumento de 10% de {moeda.moeda(pre)} é {moeda.moeda(moeda.aumenta(pre, 10))}')