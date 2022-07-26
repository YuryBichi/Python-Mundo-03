import moeda


moeda.titulo('Trabalhando com modulos.')
preço = float(input('Digite o preço: '))
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'O aumento de 10% de {preço} é {moeda.aumenta(preço, 10)}')