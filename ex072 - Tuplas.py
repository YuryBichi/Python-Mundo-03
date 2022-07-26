numero = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',\
         'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte'
escolha = int(input('Informe numero de 0 a 20: '))
while escolha < 0 or escolha > 20:
    escolha = int(input('Tente novamente. Informe numero de 0 a 20: '))
print(f'O numero \033[;31m{escolha}\033[m por extenço é \033[;31m{numero[escolha]}\033[m!')
